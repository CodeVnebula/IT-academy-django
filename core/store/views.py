from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category

def index(request):
    return JsonResponse({
        'message': 'This is meant to be the home page of the store app.',
        'all_products_address' : 'http://..../products/',
        'all_categories_address' : 'http://..../categories/',
        'admin_page_address' : 'http://..../admin/',
        'fake_orders_address' : 'http://..../orders/',
        'fake_order_detail_address' : 'http://..../orders/index/',
        })

def products_list(request):
    all_products = Product.objects.all()
    products_list = []
    for product in all_products:
        products_list.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': str(product.price),
            'categories' : [
                {'id': category.id, 'name' : category.name} 
                for category in product.category.all()
                ] if product.category else 'no category',
            'created_at': product.created_at,
            'updated_at': product.updated_at,
            'is_active': 'active' if product.is_active else 'inactive',
            'image': product.image.url,
            'stock': product.stock,
            'available': 'available' if product.available else 'not available'
        })
    
    return JsonResponse(products_list, safe=False, status=200)
    

def categories_list(request):
    all_categories = Category.objects.all()
    categories_list = []
    for category in all_categories:
        categories_list.append({
            'id': category.id,
            'name': category.name,
            'parent': {
                'id': category.parent.id,
                'name': category.parent.name
            } if category.parent else 'no parent'
        })
    
    return JsonResponse(categories_list, safe=False, status=200)
