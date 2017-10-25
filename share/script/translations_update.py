import os
import sys
import csv
# from urllib.request import urlopen

# # import re
# import datetime
# import json
# import codecs
# from pytz import timezone

# with codecs.open(ARTICLE_DATA_PATH, 'r', 'utf-8') as infile:
#     data = json.load(infile)


OUTPUT_FOLDER = os.environ.get('UNAWE_BASE') + 'spacescoop/locale'
filename = os.environ.get('UNAWE_BASE') + 'spacescoop/share/translations.csv'
# url = 'https://docs.google.com/spreadsheet/ccc?key=10lLgvZnX0eW6mR2gusvTHYqWA6PXEOMLa9af6w3xwvI&gid=633367598&output=csv'

LC_MESSAGE = '''
msgid "%s"
msgstr "%s"
'''
PREAMBLE = '''msgid ""
msgstr ""
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"

'''

TODO = '''
[Read more Space Scoops] based on INSTITUTION_NAME Press Releases
"<a href=\"%(partner_detail_url)s\">Read more Space Scoops</a> based on %(partner_name)s Press Releases."

[Learn more] about INSTITUTION_NAME
"<a href=\"%(partner_url)s\" target=\"_blank\">Learn more</a> about %(partner_name)s."

This Space Scoop is based on a Press Release from INSTITUTION_NAME

This Space Scoop is based on Press Releases from INSTITUTIONS_NAME

...use "Search" correctly

'''


def _clean(text):
    return text.strip().replace('"', '\\"').replace('\n', '')


translations = {}
keys = []

with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    for row_num, row in enumerate(reader):
        if row_num == 0:
            codes = row
            master = codes.index('en')
            for lang in row[master+1:]:
                if lang:
                    translations[lang] = []
        elif row_num in [1, 2, ]:
            # language names
            pass
        #elif row[0] != '':
        #    # section separator
        #    pass
        else:
            key = _clean(row[master])
            if key in keys:
            #    print('ERROR: key is duplicated: ', key)
            #    sys.exit(-1)
                #continue
                print('duplicate "%s" ' % key)
            else:
                keys.append(key)
            for col_num, item in enumerate(row):
                if col_num > master:  # skip english
                    if item:  # skip empty cells
                        lang = codes[col_num]
                        translations[lang].append([key, _clean(item)])

# print(translations['pt'])

for lang in translations:
    print(lang)
    path = os.path.join(OUTPUT_FOLDER, lang, 'LC_MESSAGES')
    os.makedirs(path, exist_ok=True)
    filename = os.path.join(path, 'django.po')
    with open(filename, encoding='utf-8', mode='w') as langfile:
        langfile.write(PREAMBLE)
        for x, y in translations[lang]:
            langfile.write(LC_MESSAGE % (x, y))
