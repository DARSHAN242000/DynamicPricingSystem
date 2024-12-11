from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    base_price = models.FloatField()

    def get_price(self, quantity=1):
        return self.base_price * quantity


class SeasonalProduct(Product):
    season_discount = models.FloatField(default=0.2)

    def get_price(self, quantity=1):
        return super().get_price(quantity) * (1 - self.season_discount)


class BulkProduct(Product):
    def get_price(self, quantity=1):
        if 10 <= quantity <= 20:
            discount = 0.05
        elif 21 <= quantity <= 50:
            discount = 0.1
        elif quantity > 50:
            discount = 0.15
        else:
            discount = 0
        return super().get_price(quantity) * (1 - discount)


class PremiumProduct(Product):
    premium_discount = models.FloatField(default=0.15)

    def get_price(self, quantity=1):
        return super().get_price(quantity) * (1 + self.premium_discount)
