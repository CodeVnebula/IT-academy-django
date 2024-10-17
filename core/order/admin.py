from django.contrib import admin
from .models import UserCart

@admin.register(UserCart)  
class UserCartAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user']
