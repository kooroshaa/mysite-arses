from mainpages.views import index,about,contact
from django.urls import path, include

app_name = 'mainpages'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about,name='about'),
    path('contact/', contact, name='contact')
]