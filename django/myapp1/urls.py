from django.contrib import admin
from django.urls import path
from myapp1.views import * 
urlpatterns = [
   path("",index,name="index"),
   path("about", about , name="about"),
   path("contact",contact,name="contact"),
   path("service",service,name="service")
]
