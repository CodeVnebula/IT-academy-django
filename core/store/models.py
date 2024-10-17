from django.db import models
import os

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(default='', null=False)
    
    def __str__(self):
        return f'{self.parent}/{self.name}' if self.parent else self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    slug = models.SlugField(default='', null=False)
        
    def delete(self, *args, **kwargs):
        if self.image and os.path.exists(self.image.path):
            os.remove(self.image.path)
        
        super().delete(*args, **kwargs)
        
    def __str__(self):
        return self.name
