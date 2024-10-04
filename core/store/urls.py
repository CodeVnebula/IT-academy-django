from django.urls import path
from .views import product_list, product_detail, index

urlpatterns = [
    path('', index),
    path('store/', product_list),
    path('store/<int:product_id>/', product_detail),
]