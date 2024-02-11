from django.core.management import BaseCommand
from django.db.models import Count, Avg
from ...models import Comic, Rating


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Start Average')

        result_rating = Rating.objects.filter(comic_id='2').aggregate(
            Avg('value')
        )
        result_count = Rating.objects.filter(comic_id='1').aggregate(
            Count('id')
        )
        print(result_rating, result_count)
        self.stdout.write('Done')
