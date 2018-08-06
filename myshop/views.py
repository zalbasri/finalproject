from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

def index(request):
    context = {
        "shoes": Product.objects.filter(category="Shoes", gender="Female", available=True)
    }

    return render(request, "myshop/index.html", context)