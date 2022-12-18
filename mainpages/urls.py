from mainpages.views import home,about,contact
from django.urls import path, include

urlpatterns = [
    path('home/', home),
    path('about/', about),
    path('contact/', contact)
]