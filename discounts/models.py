from django.db import models


class Discount(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField()

    def apply_discount(self, price):
        return price

    def __str__(self):
        return self.name


class PercentageDiscount(Discount):
    percentage = models.FloatField(default=0.1)

    def apply_discount(self, price):
        return price * (1 - self.percentage)


class FixedAmountDiscount(Discount):
    amount = models.FloatField()

    def apply_discount(self, price):
        return max(price - self.amount, 0)


class TieredDiscount(Discount):
    def apply_discount(self, price, total_value=None, quantity=None):
        if total_value:
            if 500 <= total_value <= 1000:
                return price * 0.95
            elif total_value > 1000:
                return price * 0.90
        elif quantity:
            if 10 <= quantity <= 20:
                return price * 0.95
            elif 21 <= quantity <= 50:
                return price * 0.90
            elif quantity > 50:
                return price * 0.85
        return price
