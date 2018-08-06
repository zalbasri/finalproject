from django.db import models

# Create your models here.

class Product(models.Model):
    gender = models.CharField(max_length=10, default='Female')
    category = models.CharField(max_length=60, default='Dress')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sizes = models.CharField(max_length=60, default='S M L')
    photo = models.ImageField(upload_to='products')
    available = models.BooleanField(default=True)

    def __str__(self):
        return f" category: {self.gender} {self.category} product: {self.name} prices {self.price} sizes: {self.sizes}"