from django.conf.urls import include, url
from django.contrib import admin
from .views import home,contact,about

urlpatterns = [


   url(r'home/',home,name="home"),
   url(r'about/',about,name="about"),
   url(r'contact/',contact,name="contact"),
]
