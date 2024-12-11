from rest_framework import serializers

from .models import Product, SeasonalProduct, BulkProduct, PremiumProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'base_price']


class SeasonalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonalProduct
        fields = ['id', 'name', 'base_price', 'season_discount']


class BulkProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkProduct
        fields = ['id', 'name', 'base_price']


class PremiumProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumProduct
        fields = ['id', 'name', 'base_price', 'premium_discount']
