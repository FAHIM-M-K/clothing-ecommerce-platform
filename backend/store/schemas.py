from ninja import ModelSchema, FilterSchema
from .models import Category, Product, ProductImage, ProductVariant
from typing import List


class ProductFilterSchema(FilterSchema):
    category__slug: str=None
    
class CategorySchema(ModelSchema):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductImageSchema(ModelSchema):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductVariantSchema(ModelSchema):
    class Meta:
        model = ProductVariant
        fields = ['id', 'size', 'color', 'stock']

class ProductSchema(ModelSchema):
    # We're telling the schema to find the related
    # category, images, and variants and use their schemas
    category: CategorySchema
    images: List[ProductImageSchema]
    variants: List[ProductVariantSchema]

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category']

    @staticmethod
    def resolve_category(obj: Product):
        return obj.category

    @staticmethod
    def resolve_image(obj: Product):
        return obj.images.all()

    @staticmethod
    def resolve_variants(obj: Product):
        return obj.variants.all()
