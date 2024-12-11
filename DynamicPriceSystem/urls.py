from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('discounts/', include('discounts.urls')),
    path('orders/', include('orders.urls'))
]
