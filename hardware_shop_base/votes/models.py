from django.db import models
from django.contrib.auth.models import User
from accounts.models import  Customer
from products.models import Product

class Vote(models.Model):
    # Vote model
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    rating = models.PositiveBigIntegerField(null=False)


    def __str__(self):
        return self.rating
    

class Product_Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment