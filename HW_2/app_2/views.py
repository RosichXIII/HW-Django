from django.shortcuts import render
from django.http import HttpResponse
import logging

from app_2.models import Order, Customer, Product

logger = logging.getLogger(__name__)

def index(request):
    description_main = '''
    <h1>Main page</h1>
    '''
    logger.info("Visited page 'Index'")
    return HttpResponse(description_main)

def orders(request):
    logger.info("Visited page 'Orders'")
    order = Order.objects.all()
    return HttpResponse(order)