from rest_framework import viewsets

from .models import Discount, PercentageDiscount, FixedAmountDiscount, TieredDiscount
from .serializers import (
    DiscountSerializer,
    PercentageDiscountSerializer,
    FixedAmountDiscountSerializer,
    TieredDiscountSerializer,
)


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class PercentageDiscountViewSet(viewsets.ModelViewSet):
    queryset = PercentageDiscount.objects.all()
    serializer_class = PercentageDiscountSerializer


class FixedAmountDiscountViewSet(viewsets.ModelViewSet):
    queryset = FixedAmountDiscount.objects.all()
    serializer_class = FixedAmountDiscountSerializer


class TieredDiscountViewSet(viewsets.ModelViewSet):
    queryset = TieredDiscount.objects.all()
    serializer_class = TieredDiscountSerializer
