from django.urls import path, include
from rest_framework import routers

from .views import InventoryView, CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = router.urls

urlpatterns.append(
    path('web', InventoryView.as_view(), name='inventory_index'),
)
