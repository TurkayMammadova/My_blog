
from django.contrib import admin
from django.urls import path,include

from .views import *

app_name='articles'

urlpatterns = [
    path('dashboard/',dashboard, name = "dashboard"), 
    path('addarticles/',addarticles, name = "addarticles"), 
    path('detail/<int:id>',detail, name = "detail"), 
    path('update/<int:id>',update, name = "update"), 
    path('delete/<int:id>',delete, name = "delete"), 
    path('comment/<int:id>',comment, name = "comment"), 
    path('',articles, name = "articles"), 



]