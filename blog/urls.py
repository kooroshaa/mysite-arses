from blog.views import index,blog_single
from django.urls import path, include

app_name = 'blog'
urlpatterns = [
    path('', index, name='blog'),
    path('single', blog_single,name='single'),
    
]