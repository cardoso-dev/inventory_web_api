from rest_framework import viewsets

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


class ProductsAjax(View):

    def get(self, *args, **kwargs):
        random_data = Product.objects.order_by('?')[:3]
        list_data = []

        for model in random_data:
            list_data.append(model_to_dict(model))

        return JsonResponse(list_data, safe=False)
