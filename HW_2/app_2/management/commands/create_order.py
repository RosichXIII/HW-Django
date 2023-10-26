from django.core.management.base import BaseCommand
from app_2.models import Order, Customer, Product

class Command(BaseCommand):
    help = 'Создать заказ, указав аргументы через пробел: первое значение - ID клиента, остальные значения - ID товара'

    def add_arguments(self, parser):
        parser.add_argument('user', type=int)
        parser.add_argument('prod', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        user = kwargs['user']
        products_cart = kwargs['prod']
        total = 0
        client = Customer.objects.get(pk=user)
        order = Order.objects.create(customer=client, price_total_order=total)
        for i in products_cart:
            order.products.add(Product.objects.get(pk=i))
            total += Product.objects.get(pk=i).price
            order.save()
        order.price_total_order = total
        order.save()
