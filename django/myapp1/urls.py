
from django.contrib import admin
from django.urls import path
from myapp1.views import * 
urlpatterns = [
   path("",index,name="index")
]
