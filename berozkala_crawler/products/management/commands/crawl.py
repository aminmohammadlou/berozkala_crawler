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
            categories = category_crawler()
            for category in categories:
                category.save()
        elif arg == 'product':
            categories = Category.objects.all()
            for category in categories:
                products = product_crawler(category)
                for product in products:
                    product.save()
        else:
            raise CommandError(f'Argument "{arg}" Is Invalid')
