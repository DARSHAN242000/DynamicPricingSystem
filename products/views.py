from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product, SeasonalProduct, BulkProduct, PremiumProduct
from .serializers import ProductSerializer, SeasonalProductSerializer, BulkProductSerializer, PremiumProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SeasonalProductViewSet(viewsets.ModelViewSet):
    queryset = SeasonalProduct.objects.all()
    serializer_class = SeasonalProductSerializer

    @action(detail=True, methods=['get'], url_path='real-time-price')
    def get_real_time_price(self, request, pk=None):
        """
        Retrieve real-time price of a premium product based on the quantity
        """
        quantity = int(request.query_params.get('quantity', 1))

        try:
            seasonal_product = SeasonalProduct.objects.get(pk=pk)
        except SeasonalProduct.DoesNotExist:
            return Response({'error': 'Seasonal Product not found'}, status=status.HTTP_404_NOT_FOUND)

        price = seasonal_product.get_price(quantity=quantity)
        return Response({
            'bulk_product_id': seasonal_product.id,
            'name': seasonal_product.name,
            'base_price': seasonal_product.base_price,
            'season_discount': seasonal_product.season_discount,
            'quantity': quantity,
            'final_price': price
        })


class BulkProductViewSet(viewsets.ModelViewSet):
    queryset = BulkProduct.objects.all()
    serializer_class = BulkProductSerializer

    @action(detail=True, methods=['get'], url_path='real-time-price')
    def get_real_time_price(self, request, pk=None):
        """
        Retrieve real-time price of a bulk product based on the quantity
        """
        quantity = int(request.query_params.get('quantity', 1))

        try:
            bulk_product = BulkProduct.objects.get(pk=pk)
        except BulkProduct.DoesNotExist:
            return Response({'error': 'Bulk Product not found'}, status=status.HTTP_404_NOT_FOUND)

        price = bulk_product.get_price(quantity=quantity)
        return Response({
            'bulk_product_id': bulk_product.id,
            'name': bulk_product.name,
            'base_price': bulk_product.base_price,
            'quantity': quantity,
            'final_price': price
        })


class PremiumProductViewSet(viewsets.ModelViewSet):
    queryset = PremiumProduct.objects.all()
    serializer_class = PremiumProductSerializer

    @action(detail=True, methods=['get'], url_path='real-time-price')
    def get_real_time_price(self, request, pk=None):
        """
        Retrieve real-time price of a premium product based on the quantity
        """
        quantity = int(request.query_params.get('quantity', 1))

        try:
            premium_product = PremiumProduct.objects.get(pk=pk)
        except PremiumProduct.DoesNotExist:
            return Response({'error': 'Premium Product not found'}, status=status.HTTP_404_NOT_FOUND)

        price = premium_product.get_price(quantity=quantity)
        return Response({
            'bulk_product_id': premium_product.id,
            'name': premium_product.name,
            'base_price': premium_product.base_price,
            'premium_discount': premium_product.premium_discount,
            'quantity': quantity,
            'final_price': price
        })
