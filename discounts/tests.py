from django.test import TestCase

from .models import PercentageDiscount, FixedAmountDiscount, TieredDiscount


class DiscountModelTest(TestCase):
    def setUp(self):
        self.percentage_discount = PercentageDiscount.objects.create(name="10% Off", priority=1, percentage=0.10)
        self.fixed_discount = FixedAmountDiscount.objects.create(name="$50 Off", priority=2, amount=50)
        self.tiered_discount = TieredDiscount.objects.create(name="Tiered Discount", priority=3)

    def test_percentage_discount(self):
        price = 100
        discounted_price = self.percentage_discount.apply_discount(price)
        self.assertEqual(discounted_price, 90)

    def test_fixed_amount_discount(self):
        price = 100
        discounted_price = self.fixed_discount.apply_discount(price)
        self.assertEqual(discounted_price, 50)

    def test_tiered_discount_value_based(self):
        price = 1000
        discounted_price = self.tiered_discount.apply_discount(price, total_value=1000)
        self.assertEqual(discounted_price, 950)
