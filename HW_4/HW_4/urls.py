"""
URL configuration for HW_4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_4 import views

urlpatterns = [
    # path("", views.index, name='index'),
    path('admin/', admin.site.urls),
    path("orders/", views.orders, name='orders'),
    path("", views.index_base, name='index_base'),
    path("customer_orders/<int:customer_id>", views.customer_orders, name='customert_orders'),
    path("order/<int:order_id>", views.order, name='order'),
    path("customer_orders_long/<int:customer_id>", views.customer_orders_long, name='customer_orders_long'),
    path("orders_by_days/<int:customer_id>/<int:count_day>", views.orders_by_days, name='orders_by_dayss'),
    path('product_form/<int:id_product>', views.product_form, name='product_form'),
    path('select_product_by_id/', views.select_product_by_id, name='select_product_by_id'),
    path('select_products_by_client_by_days/', views.select_products_by_client_by_days, name='select_products_by_client_by_days'),
    path('select_product/', views.select_product, name='select_product'),
]