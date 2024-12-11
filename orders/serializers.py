from rest_framework import serializers

from discounts.serializers import DiscountSerializer
from products.serializers import ProductSerializer
from .models import Order, OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderProduct
        fields = ['id', 'product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(source='orderproduct_set', many=True)
    discounts = DiscountSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'products', 'discounts', 'total_price']

    def get_total_price(self, obj):
        return obj.calculate_total()
