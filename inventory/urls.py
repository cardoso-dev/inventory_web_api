from django.contrib import admin
from django.urls import path

from .views import InventoryView

urlpatterns = [
    path('', InventoryView.as_view(), name='inventory_index'),
]
