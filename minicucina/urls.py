
from django.urls import path, include
from django import views
from .views import *

urlpatterns = [
    path('', home, name="home"),
]
