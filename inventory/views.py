from rest_framework import viewsets

from rest_framework import generics
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.generic import TemplateView, View

from .models import Category, Product

from.serializers import CategorySerializer, ProductSerializer


class InventoryView(TemplateView):
    template_name = "inventory/inventory.html"

    def get_context_data(self, **kwargs):
        context = super(InventoryView, self).get_context_data(**kwargs)

        context['products'] = Product.objects.all()

        return context


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsRandomList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.order_by('?')[:3]
        return queryset
