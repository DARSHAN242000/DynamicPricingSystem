from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Order, OrderProduct
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        products = data.pop('products', [])
        discounts = data.pop('discounts', [])

        order = Order.objects.create()
        for discount_id in discounts:
            order.discounts.add(discount_id)

        for product_data in products:
            OrderProduct.objects.create(
                order=order,
                product_id=product_data['product_id'],
                quantity=product_data['quantity']
            )

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'], url_path='calculate-total')
    def calculate_total(self, request, pk=None):
        try:
            order = self.get_object()
            total = order.calculate_total()
            return Response({'order_id': order.id, 'total_price': total})
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
