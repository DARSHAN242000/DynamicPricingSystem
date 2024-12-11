from django.db import models

from discounts.models import Discount
from products.models import Product


class Order(models.Model):
    products = models.ManyToManyField(Product, through='OrderProduct')
    discounts = models.ManyToManyField(Discount)

    def calculate_total(self):
        total = sum([item.product.get_price(item.quantity) for item in self.orderproduct_set.all()])
        for discount in self.discounts.order_by('priority'):
            total = discount.apply_discount(total)
        return total

    def __str__(self):
        return f"Order {self.id}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
