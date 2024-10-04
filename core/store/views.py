from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return JsonResponse({'message': 'Hello, World!'})

def product_list(request):
    products = [
        {
            'id': 1,
            'name': 'Product 1',
            'description': 'Description for Product 1',
            'price': 10.99
        },
        {
            'id': 2,
            'name': 'Product 2',
            'description': 'Description for Product 2',
            'price': 15.49
        },
        {
            'id': 3,
            'name': 'Product 3',
            'description': 'Description for Product 3',
            'price': 8.99
        },
    ]
    return JsonResponse(products, safe=False)

def product_detail(request, product_id):
    product_details = {
        1: {
            'id': 1,
            'name': 'Product 1',
            'description': 'Description for Product 1',
            'price': 10.99
        },
        2: {
            'id': 2,
            'name': 'Product 2',
            'description': 'Description for Product 2',
            'price': 15.49
        },
        3: {
            'id': 3,
            'name': 'Product 3',
            'description': 'Description for Product 3',
            'price': 8.99
        },
    }
    
    product = product_details.get(product_id, {'error': 'Product not found'})
    return JsonResponse(product)