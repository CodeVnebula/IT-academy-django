from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import categories_list, products_list, index

urlpatterns = [
    path('', index),
    path('categories/', categories_list),
    path('products/', products_list),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    