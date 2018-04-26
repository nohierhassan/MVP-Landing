from django.conf.urls import include, url
from django.contrib import admin
from .views import home,contact,about

urlpatterns = [


   url(r'home/',home,name="home"),
   url(r'signup/',about,name="signup"),
   url(r'contact/',contact,name="contact"),
]
