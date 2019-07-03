from django.conf.urls import url, include
from rest_framework import routers

from .views import InventoryView, CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(
    r'api/categories', CategoryViewSet)
router.register(
    r'api/products', ProductViewSet)

urlpatterns = [
    url('^$', InventoryView.as_view(), name='inventory_index'),
    url(r'^', include(router.urls)),
]
