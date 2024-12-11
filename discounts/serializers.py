from rest_framework import serializers

from .models import Discount, PercentageDiscount, FixedAmountDiscount, TieredDiscount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'name', 'priority']


class PercentageDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PercentageDiscount
        fields = ['id', 'name', 'priority', 'percentage']


class FixedAmountDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedAmountDiscount
        fields = ['id', 'name', 'priority', 'amount']


class TieredDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TieredDiscount
        fields = ['id', 'name', 'priority']
