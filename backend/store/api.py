from typing import List
from ninja import Router, Query
from .models import Product
from .schemas import ProductSchema, ProductFilterSchema
from django.shortcuts import get_object_or_404

# Create a 'router' instance. We'll attach all our store endpoints to this
router = Router()

@router.get("/products", response=List[ProductSchema])
def list_products(request,filters:ProductFilterSchema=Query(...)):
    # 1. Get all products
    products = Product.objects.all()
    # Apply the filters
    products=filters.filter(products)
    # 2. Optimize the query
    products = products.select_related('category').prefetch_related('images', 'variants')
    
    return products

@router.get("/products/{product_id}",response=ProductSchema)
def get_product(request,product_id:int):
    product=get_object_or_404(Product,id=product_id)
    return product