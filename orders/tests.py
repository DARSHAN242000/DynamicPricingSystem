from django.test import TestCase
from products.models import Product
from discounts.models import Discount, PercentageDiscount
from .models import Order, OrderProduct


class OrderModelTest(TestCase):
    def setUp(self):
        # Create sample products
        self.product1 = Product.objects.create(name="Basic Product", base_price=100)
        self.product2 = Product.objects.create(name="Premium Product", base_price=200)

        # Create discounts
        self.discount = PercentageDiscount.objects.create(name="10% Off", priority=1, percentage=0.10)

        # Create order
        self.order = Order.objects.create()
        self.order.discounts.add(self.discount)
        OrderProduct.objects.create(order=self.order, product=self.product1, quantity=2)
        OrderProduct.objects.create(order=self.order, product=self.product2, quantity=1)

    def test_calculate_total(self):
        total = self.order.calculate_total()
        self.assertEqual(total, 400.0)
