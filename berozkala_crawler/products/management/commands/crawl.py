from django.core.management import BaseCommand, CommandError

from products.utils.crawler import product_crawler, category_crawler

from products.models import Category


class Command(BaseCommand):
    help = "Crawls Berozkala.com"

    def add_arguments(self, parser):
        parser.add_argument('arg')

    def handle(self, *args, **options):
        arg = options['arg']
        if arg == 'category':
            category_crawler()
        elif arg == 'product':
            categories = Category.objects.all().exclude(pk=1)
            for category in categories:
                product_crawler(category)
        else:
            raise CommandError(f'Argument "{arg}" Is Invalid')
