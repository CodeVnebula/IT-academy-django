from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.top_level_categories, name='top_level_categories'),
    path('categories/<int:category_id>/products/', views.category_product_list, name='category_product_list'),
    path('categories/<int:category_id>/products/<int:product_id>/', views.product_details, name='product_details'),
] 
   