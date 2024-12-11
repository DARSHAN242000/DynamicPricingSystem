from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiscountViewSet, PercentageDiscountViewSet, FixedAmountDiscountViewSet, TieredDiscountViewSet

router = DefaultRouter()
router.register('discounts', DiscountViewSet)
router.register('percentage-discounts', PercentageDiscountViewSet)
router.register('fixed-amount-discounts', FixedAmountDiscountViewSet)
router.register('tiered-discounts', TieredDiscountViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
