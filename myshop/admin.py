from django.contrib import admin
from .models import Product, Comment, Cart

# Register your models here.
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Cart)