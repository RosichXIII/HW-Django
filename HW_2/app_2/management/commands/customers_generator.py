from django.core.management.base import BaseCommand
from app_2.models import Customer

class Command(BaseCommand):
    help = 'Генерация клиентов'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Customer(name=f'Name_probable{i}',
                            email=f'smth{i}@mail.com',
                            phone=f'{8008008 + i}',
                            address=f'somewhere{i}')
            client.save()