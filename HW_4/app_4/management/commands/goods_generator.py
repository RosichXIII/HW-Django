from django.core.management.base import BaseCommand
from random import randint
from app_4.models import Product

class Command(BaseCommand):
    help = 'Генерация товаров'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(product_name=f'MegaProduct_{i}',
                              product_description=f'AmazingInfo {i}',
                              price=f'{i*(randint(100, 50001)/100)}',
                              product_quantity=f'{randint(i, i*3)}')
            product.save()