from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.parent}/{self.name}' if self.parent else self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/products/', null=True, blank=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
