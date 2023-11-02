from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from datetime import timedelta, timezone
import logging

from app_4.models import *
from app_4.forms import *

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
    return render(request, 'app_4/index.html')

def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_id = Order.objects.get(pk=order_id).pk
    date_order = Order.objects.get(pk=order_id).date_order
    customer = Order.objects.get(pk=order_id).customer.name
    price_total_order = Order.objects.get(pk=order_id).price_total_order
    products = Order.objects.get(pk=order_id).products.all()

    return render(
        request, 'app_4/order.html', {'order': order, 'order_id': order_id,
                                      'date_order': date_order, 'products': products,
                                      'customer': customer, 'price_total_order': price_total_order,})

def customer_orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'app_4/customer_orders.html',
                  {'customer': customer, 'orders': orders})

def customer_orders_long(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'app_4/customer_orders_long.html',
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
        request, 'app_4/orders_by_days.html',
                {'count_day': count_day, 'customer': customer, 'list_filter_orders': list_filter_orders, })
    
    
# _______________________________


def product_form(request, product_id: int):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.product_name = request.POST["product_name"]
            product.product_description = request.POST["product_description"]
            product.price = request.POST["price"]
            product.product_quantity = request.POST["product_quantity"]
            product_img = form.cleaned_data['product_img']
            if "product_img" in request.FILES:
                product.product_img_product = request.FILES["product_img"]
            product.save()
            logger.info(f"Product {product.product_name} is changed successfully")
            return redirect("product", product_id=product.id)
    else:
        form = ProductForm()

    context = {
        "form": form,
        "product": product,
    }
    return render(request, "app_4/product_form.html", context=context)


def select_product_by_id(request):
    if request.method == "POST":
        form = SelectProductById(request.POST, request.FILES)
        if form.is_valid():
            product_id = request.POST['product_id']
            return redirect("product_form", product_id)
    else:
        form = SelectProductById()

    context = {
        "form": form
    }
    return render(request, "app_4/select_product_by_id.html", context=context)


def select_products_by_client_by_days(request):
    if request.method == "POST":
        form = SelectProductByCustomerBydays(request.POST, request.FILES)
        if form.is_valid():
            customer_id = request.POST['customer_id']
            days = request.POST['days']

            return redirect("client_products_sorted", customer_id, days)
    else:
        form = SelectProductByCustomerBydays()

    context = {
        "form": form
    }
    return render(request, "app_4/select_products_by_days.html", context=context)

def select_product(request):
    if request.method == "POST":
        form = SelectProductById(request.POST, request.FILES)
        if form.is_valid():
            product_id = request.POST['product_id']

            return redirect("product", product_id)
    else:
        form = SelectProductById()

    context = {
        "form": form
    }
    return render(request, "app_4/select_product_by_id.html", context=context)