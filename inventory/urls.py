from django.urls import path
from . import views

urlpatterns = [
    path('inventory/<int:id>', views.inbound_create, name='inventory'),
]