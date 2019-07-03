from rest_framework import viewsets

from django.views.generic import TemplateView

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
