from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'blogs/blog-home.html')

def blog_single(request):
    return render(request, 'blogs/blog-single.html')

