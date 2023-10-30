from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from datetime import timedelta, timezone
import logging

from app_3.models import Order, Customer, Product

logger = logging.getLogger(__name__)

# def index(request):
#     description_main = '''
#     <h1>Main page</h1>
#     '''
#     logger.info("Visited page 'Index'")
#     return HttpResponse(description_main)

def orders(request):
    logger.info("Visited page 'Orders'")
    order = Order.objects.all()
    return HttpResponse(order)

def index_base(request):
    return render(request, 'app_3/index.html')

def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_id = Order.objects.get(pk=order_id).pk
    date_order = Order.objects.get(pk=order_id).date_order
    customer = Order.objects.get(pk=order_id).customer.name
    price_total_order = Order.objects.get(pk=order_id).price_total_order
    products = Order.objects.get(pk=order_id).products.all()

    return render(
        request, 'app_3/order.html', {'order': order, 'order_id': order_id,
                                      'date_order': date_order, 'products': products,
                                      'customer': customer, 'price_total_order': price_total_order,})

def customer_orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'app_3/customer_orders.html',
                  {'customer': customer, 'orders': orders})

def customer_orders_long(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'app_3/customer_orders_long.html',
                  {'customer': customer, 'orders': orders,})

def orders_by_days(request, customer_id, count_day):
    customer = get_object_or_404(Customer, pk=customer_id)
    all_orders = Order.objects.filter(customer=customer)
    date_now = timezone.now()
    start_date = date_now - timedelta(days=count_day)
    list_filter_orders = []
    for order in all_orders:
        if start_date <= order.date_order:
            list_filter_orders.append(order)
    return render(
        request, 'app_3/orders_by_days.html',
                {'count_day': count_day, 'customer': customer, 'list_filter_orders': list_filter_orders, })
