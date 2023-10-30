from django.core.management.base import BaseCommand
from app_3.models import Order

class Command(BaseCommand):
    help = 'Просмотр заказа по ID (PK)'

    def add_arguments(self, parser):
        parser.add_argument('id_order', type=int)

    def handle(self, *args, **kwargs):
        id_order = kwargs['id_order']
        order = Order.objects.get(pk=id_order)
        print(order)
        order.save()