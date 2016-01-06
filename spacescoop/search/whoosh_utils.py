import os

from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.columns import RefBytesColumn
from whoosh.qparser import QueryParser, MultifieldParser, WildcardPlugin
from whoosh.analysis import StemmingAnalyzer, CharsetFilter
from whoosh.sorting import Facets, StoredFieldFacet, FieldFacet
from whoosh.support.charset import accent_map
from django.conf import settings

from spacescoop_shared.articles.models import Article


def _get_schema():
    analyzer = StemmingAnalyzer() | CharsetFilter(accent_map)  # WARN: stemming is english specific; character folding is for western languages
    schema = Schema(code = ID(unique=True, stored=True), 
                    slug = ID(unique=False, stored=True), 
                    title = TEXT(analyzer=analyzer, stored=True), 
                    content = TEXT(analyzer=analyzer),

                    # teaser = STORED(),
                    # theme = STORED(),
                    # age_range = STORED(),
                    # release_date = STORED(),
                    # author_list = STORED(),
                    # code = STORED(),
                    # main_visual = STORED(),
                    # thumb2_url = STORED(),

                    )
    return schema


class LanguageIndex(object):
    index = None
    # writer = None  # keep a writer for bulk updates

    def __init__(self, lang):
        self.lang = lang

    def _get_path(self):
        return os.path.join(settings.WHOOSH_INDEX_PATH, self.lang)

    def clear(self):
        '''create index from scratch; creates a writer too.'''

        index_path = self._get_path()
        if not os.path.exists(index_path):
            os.makedirs(index_path)
        self.index = create_in(index_path, _get_schema())

        writer = self.index.writer()
        ## optimize analyzer for batch updates
        # analyzer = writer.schema['content'].format.analyzer
        # analyzer.cachesize = -1
        # analyzer.clear()
        from whoosh.analysis.morph import StemFilter
        analyzer = writer.schema['content'].analyzer
        for item in analyzer.items:
            if isinstance(item, StemFilter):
                item.cachesize = -1
                item.clear()
        writer.commit()
        # self.writer = writer

    def load(self):
        '''load an existing index'''
        self.index = open_dir(self._get_path())
        return self.index
        # return open_dir(self._get_path())

    def get_writer(self):
        # if not self.writer:
        #     self.writer = self.index.writer()
        # return self.writer
        return self.index.writer()

    # def close_writer(self):
    #     if self.writer:
    #         self.writer.close()
    #         self.writer = None


def _remove_html_tags(data):
    import re
    p = re.compile(r'<.*?>')
    return p.sub('', data)


def _content(obj):
    # TODO: remove markup
    return '\n\n\n'.join([
        # obj.title,
        _remove_html_tags(obj.story),
        # bleach.clean(obj.story, tags=None, strip=True),
        str(obj.cool_fact),
    ])


def rebuild_indexes():
    try:
        writers = {}
        for obj_master in Article.objects.available():
            for obj in obj_master.translations.all():
                lang = obj.language_code
                if not lang in writers:
                    index = LanguageIndex(lang)
                    index.clear()
                    writers[lang] = index.get_writer()
                _update_article(obj_master, obj, writer=writers[lang])
    finally:
        for writer in writers.values():
            writer.commit()


def _update_article(obj_master, obj, writer):
    writer.update_document(code=obj_master.code, slug=obj.slug, title=obj.title, content=_content(obj), )


def update_article(obj_master):
    indexes = LanguageIndexes()
    for obj in obj_master.translations.all():
        with indexes[obj.language_code].get_writer() as writer:
            _update_article(obj, writer=writer)


def remove_article(obj):
    #TODO
    pass




def search(querystring, language_code):
    ix = LanguageIndex(language_code).load()
    # parser = QueryParser('content', ix.schema)
    parser = MultifieldParser(['title', 'keywords', 'content'], ix.schema)  # fieldboosts={'title':5, 'keywords':4, 'content':1})
    parser.remove_plugin_class(WildcardPlugin)  # remove unused feature for better performance
    query = parser.parse(querystring)

    result = {
        'results': [],
    }

    with ix.searcher() as searcher:
        results = searcher.search(query)
        # import pdb; pdb.set_trace()

        # collect results
        for hit in results:
            my_hit = {}
            # my_hit['pos'] = hit.pos
            # my_hit['rank'] = hit.rank
            # my_hit['docnum'] = hit.docnum
            my_hit['score'] = hit.score
            my_hit['object'] = Article.objects.get(code=hit.fields()['code'])
            # my_hit['object']['is_visible'] = True
            result['results'].append(my_hit)
            # print hit.pos, hit.rank, hit.docnum, hit.score, hit.fields()['age_range'], hit

    return result
