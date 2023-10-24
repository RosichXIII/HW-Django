# from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    description_main = '''
    <h1>Main page</h1>
    '''
    logger.info("Visit page main")
    return HttpResponse(description_main)

def about(request):
    description_about = '''
    <h2>About</h2>
    '''
    logger.info("Visit page about")
    return HttpResponse(description_about)