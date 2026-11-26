from django.db import models as m
from django.contrib.auth.models import User

class Category(m.Model):
    name = m.CharField(max_length=50, verbose_name="Category name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Product(m.Model):
    name = m.CharField(max_length=200, verbose_name="Product name")
    price = m.DecimalField(max_digits=10,decimal_places=2,verbose_name="Product price")
    description = m.CharField(max_length=1000, verbose_name="Product description")
    weight = m.DecimalField(max_digits=10, decimal_places=2, verbose_name="Product weight")
    category = m.ForeignKey(to=Category, on_delete=m.CASCADE, verbose_name="Product category")
    picture = m.ImageField(upload_to='product_pics/', verbose_name="Product picture")

    def __str__(self):
        return self.name

class UserProfile(m.Model):
    user = m.OneToOneField(User, on_delete=m.CASCADE, verbose_name="Profile User")
    profilePicture = m.ImageField(upload_to='profile_pics/', verbose_name="Profile Picture", null=True, blank=True)
    bio = m.CharField(max_length=1000, default="No biography has been written")
    phone = m.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


        
