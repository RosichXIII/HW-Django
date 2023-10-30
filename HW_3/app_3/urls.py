from django.urls import path
from app_3 import views

urlpatterns = [
    path("orders/", views.orders, name='orders'),
    path("", views.index_base, name='index_base'),
    path("customer_orders/<int:customer_id>", views.customer_orders, name='customert_orders'),
    path("order/<int:order_id>", views.order, name='order'),
    path("customer_orders_long/<int:customer_id>", views.customer_orders_long, name='customer_orders_long'),
    path("orders_by_days/<int:customer_id>/<int:count_day>", views.orders_by_days, name='orders_by_dayss')
]