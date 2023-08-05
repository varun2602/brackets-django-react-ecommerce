from django.db import models
from django.contrib.auth.models import User


# Vendor Model 
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    address = models.TextField(null = True, blank = True)

    def __str__(self):
        return f"{self.user}"

class ProductCategory(models.Model):
    title = models.CharField(max_length = 200, blank = True, null = True)
    details = models.TextField(null = True, blank = True)

    def __str__(self):
        return f"{self.title}"
    
class Products(models.Model):
    title = models.CharField(max_length = 200)
    details = models.TextField(null = True, blank = True)
    price = models.FloatField()

    def __str__(self):
        return f"{self.title}"
