from django.contrib import admin
from .models import Category, Product, ProductImage, ProductVariant, Order, OrderItem, PromotionalSlider

# Register models
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductVariant)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PromotionalSlider)
