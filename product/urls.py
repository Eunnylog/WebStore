# tweet/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product_create, name='product-create'),
    path('product_list/', views.product_list, name='product_list'),
]