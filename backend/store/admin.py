from django.contrib import admin
from .models import Category, Product, ProductVariant, Order, OrderItem

# Register models
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(Order)
admin.site.register(OrderItem)