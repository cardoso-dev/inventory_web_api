from django.conf.urls import url, include
from rest_framework import routers

from .views import InventoryView, CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(
    r'categories', CategoryViewSet, base_name ='api')
router.register(
    r'products', ProductViewSet, base_name ='api')

urlpatterns = [
    url('^$', InventoryView.as_view(), name='inventory_index'),
    url(r'^', include(router.urls)),
]
