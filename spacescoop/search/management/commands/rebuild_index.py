from django.core.management.base import BaseCommand, CommandError

# from spacescoop.activities import tasks
# from spacescoop.activities.models import Article

from spacescoop.search import whoosh_utils


class Command(BaseCommand):
    help = 'Generate Whoosh index'

    def handle(self, *args, **options):
        whoosh_utils.rebuild_indexes()
