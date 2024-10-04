from django.shortcuts import render
from django.http import JsonResponse

def order_list(request):
    orders = [
        {
            'id': 1,
            'customer_name': 'Customer 1',
            'total_amount': 29.99
        },
        {
            'id': 2,
            'customer_name': 'Customer 2',
            'total_amount': 59.99
        },
        {
            'id': 3,
            'customer_name': 'Customer 3',
            'total_amount': 19.99
        },
    ]
    return JsonResponse(orders, safe=False)

def order_detail(request, order_id):
    order_details = {
        1: {
            'id': 1,
            'customer_name': 'Customer 1',
            'total_amount': 29.99
        },
        2: {
            'id': 2,
            'customer_name': 'Customer 2',
            'total_amount': 59.99
        },
        3: {
            'id': 3,
            'customer_name': 'Customer 3',
            'total_amount': 19.99
        },
    }
    
    order = order_details.get(order_id, {'error': 'Order not found'})
    return JsonResponse(order)