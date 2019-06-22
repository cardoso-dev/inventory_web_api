from django.views.generic import TemplateView

from .models import Product


class InventoryView(TemplateView):
    template_name = "inventory/inventory.html"

    def get_context_data(self, **kwargs):
        context = super(InventoryView, self).get_context_data(**kwargs)

        context['products'] = Product.objects.all()

        return context
