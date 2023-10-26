from django.core.management.base import BaseCommand
from app_2.models import Order

class Command(BaseCommand):
    help = 'Просмотр всех заказов'

    def handle(self, *args, **kwargs):
        order = Order.objects.all()
        print(order)