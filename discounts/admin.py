from django.contrib import admin
from .models import Discount, PercentageDiscount, FixedAmountDiscount, TieredDiscount

admin.site.register(Discount)
admin.site.register(PercentageDiscount)
admin.site.register(FixedAmountDiscount)
admin.site.register(TieredDiscount)
