from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SeasonalProductViewSet, BulkProductViewSet, PremiumProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('seasonal-products', SeasonalProductViewSet)
router.register('bulk-products', BulkProductViewSet)
router.register('premium-products', PremiumProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
