from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('it is HOME!')

def about(request):
    return HttpResponse('it is ABOUT!')

def contact(request):
    return HttpResponse('it is CONTACT!')