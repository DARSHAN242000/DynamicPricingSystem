from django.test import TestCase

from .models import Product, SeasonalProduct, BulkProduct, PremiumProduct


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", base_price=100)
        self.seasonal_product = SeasonalProduct.objects.create(name="Seasonal Product", base_price=100,
                                                               season_discount=0.1)
        self.bulk_product = BulkProduct.objects.create(name="Bulk Product", base_price=100)
        self.premium_product = PremiumProduct.objects.create(name="Premium Product", base_price=100, premium_discount=0.2)

    def test_product_price(self):
        self.assertEqual(self.product.get_price(), 100)

    def test_seasonal_product_price(self):
        self.assertEqual(self.seasonal_product.get_price(), 90)

    def test_bulk_product_price(self):
        self.assertEqual(self.bulk_product.get_price(25), 2250.0)

    def test_premium_product_price(self):
        self.assertEqual(self.premium_product.get_price(), 120)
