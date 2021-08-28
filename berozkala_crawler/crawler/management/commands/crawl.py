from django.core.management import BaseCommand, CommandError

from crawler.utils.crawler import product_crawler, category_crawler


class Command(BaseCommand):
    help = "Crawls Berozkala.com"

    def add_arguments(self, parser):
        parser.add_argument('arg')

    def handle(self, *args, **options):
        arg = options['arg']
        categories = category_crawler()
        if arg == 'category':
            for category in categories:
                category.save()
        elif arg == 'product':
            for category in categories:
                products = product_crawler(category)
                for product in products:
                    product.save()
        else:
            raise CommandError(f'Argument "{arg}" Is Invalid')
