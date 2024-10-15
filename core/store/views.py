from django.core.paginator import Paginator
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product, Category
from django.db import models

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def top_level_categories(request):
    categories = Category.objects.filter(parent=None).prefetch_related(
        'product_set'
    ).annotate(products_count=models.Count('product'))
    
    categories_list = []
    for category in categories:
        categories_list.append({
            'id': category.id,
            'name': category.name,
            'products_count': category.products_count, 
        })
    
    context = {
        'addresses': {
            'CATEGORIES': 'categories',
        },
        'categories': categories_list,
    }

    # template = loader.get_template('top_level_categories.html')
    # return HttpResponse(template.render(context, request))
    return render(request, 'top_level_categories.html', context)

def category_product_list(request, category_id):
    category = Category.objects.get(id=category_id)

    products_queryset = category.product_set.annotate(
        total_cost_per_product=models.F('price') * models.F('stock')
    )
    
    product_aggregates = products_queryset.aggregate(
        most_expensive_product_price=models.Max('price'),
        cheapest_product_price=models.Min('price'),
        average_product_price=models.Avg('price'),
        total_cost=models.Sum('total_cost_per_product')
    )

    paginator = Paginator(products_queryset, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    products = []
    for product in page_obj:
        products.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'stock': product.stock,
            'available': product.available,
            'total_cost_per_product': product.total_cost_per_product,
        })

    context = {
        'page_obj': page_obj,
        'addresses': {
            'CATEGORIES': 'categories',
            'PRODUCTS': f'categories/{category_id}/products',
        },
        'products': products,
        'most_expensive_product_price': product_aggregates['most_expensive_product_price'],
        'cheapest_product_price': product_aggregates['cheapest_product_price'],
        'average_price': f"{product_aggregates['average_product_price']:.2f}",
        'total_cost': product_aggregates['total_cost'],
    }

    # template = loader.get_template('products_list.html')
    # return HttpResponse(template.render(context, request))
    return render(request, 'products_list.html', context)

def product_details(request, category_id, product_id):
    product = Product.objects.get(id=product_id)
    product_details = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'category': product.category.all().first().name,
        'created_at': product.created_at,
        'updated_at': product.updated_at,
        'is_active': product.is_active,
        'image': product.image.url,
        'stock': product.stock,
        'available': product.available,
        'slug': product.slug,
    }
    
    context = {
        'product': product_details,
        'addresses' : {
            'CATEGORIES' : 'categories',
            'PRODUCTS' : f'categories/{category_id}/products',
            'PRODUCT DETAILS' : f'categories/{category_id}/products/{product_id}',
        },
    }
    
    return render(request, 'product_details.html', context)
