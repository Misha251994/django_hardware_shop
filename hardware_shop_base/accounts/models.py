from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


class Customer(models.Model):
    """Customer model creating on basic django user model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, null=True)
    phone = PhoneField(blank=True, null=True, help_text="Contact phone number")
    profile_picture = models.ImageField(null=True, blank=True)


class Seller(models.Model):
    """Seller model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    email = models.EmailField(max_length=50)
    adress = models.CharField(max_length=50)
    phone = PhoneField(blank=True, null=False, help_text="Contact phone number")
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.company_name
