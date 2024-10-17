from django.db import models
from user.models import User

class UserCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return self.user.username
