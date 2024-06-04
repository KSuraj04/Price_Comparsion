from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.compare_product_prices, name='compare_product_prices'),
]