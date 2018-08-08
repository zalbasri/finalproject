from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    gender = models.CharField(max_length=10)
    category = models.CharField(max_length=60)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sizes = models.CharField(max_length=60, default='S M L')
    photo = models.ImageField(upload_to='products')
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"category: {self.gender} {self.category}, product: {self.name}, price: {self.price}, sizes: {self.sizes}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False, related_name='comments')
    text = models.TextField()
    time = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return f"user: {self.user}, product: {self.product}, text: {self.text}, time: {self.time}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    item = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.user} {self.product.name} {self.size}"
