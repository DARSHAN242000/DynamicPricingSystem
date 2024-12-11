from django.contrib import admin
from .models import Product, SeasonalProduct, BulkProduct, PremiumProduct

admin.site.register(Product)
admin.site.register(SeasonalProduct)
admin.site.register(BulkProduct)
admin.site.register(PremiumProduct)
