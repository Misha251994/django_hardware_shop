from django.db import models
from accounts.models import Seller


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    #Product model

    name = models.CharField(max_length=100, unique=True, null=False, verbose_name="Product name")
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False )
    product_count = models.PositiveIntegerField(null=False, default=0)
    seller = models.ForeignKey(Seller, null=False, on_delete=models.CASCADE)
    product_photo = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.name

