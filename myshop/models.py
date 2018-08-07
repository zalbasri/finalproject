from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    gender = models.CharField(max_length=10, default='Female')
    category = models.CharField(max_length=60, default='Dress')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sizes = models.CharField(max_length=60, default='S M L')
    photo = models.ImageField(upload_to='products')
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"category: {self.gender} {self.category}, product: {self.name}, prices {self.price}, sizes: {self.sizes}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False, related_name='comments')
    text = models.TextField()
    time = models.DateTimeField(auto_now=True, auto_now_add=True)


    def __str__(self):
        return f"user: {self.user}, product: {self.product}, text: {self.text}, time: {self.time}"