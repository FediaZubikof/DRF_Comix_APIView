from django.core.management import BaseCommand
from django.db.models import Count, Avg
from ...models import Comic, Rating


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Start Average')

        result = Rating.objects.filter(comic_id='2').aggregate(
            Avg('value')
        )
        print(result)
        self.stdout.write('Done')
