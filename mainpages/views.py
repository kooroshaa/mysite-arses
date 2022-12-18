from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'webpages/home.html')

def about(request):
    return render(request, 'webpages/about.html')

def contact(request):
    return render(request, 'webpages/contact.html')