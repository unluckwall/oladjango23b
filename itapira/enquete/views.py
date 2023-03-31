from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (resquest):
    return HttpResponse('seila, lukita')

def flasco (resquest):
    return HttpResponse('Uniao flasco, nova ordem mudial')
