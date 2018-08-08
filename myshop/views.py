from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from myshop.forms import RegisterationForm # registeration form created
from .models import Product, Comment, Cart


def index(request):
    user = request.user
    context = {
        "user": user,
        "firstpage": True
    }
    return render(request, "myshop/index.html", context)


def login_view(request):
    if request.method == 'POST':
        # gets the filled login form from the html
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    # if request method is get, sends an non-filled login form
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'myshop/login.html', context)


def logout_view(request):
    cart = request.session.get('cart', [])
    for item in cart:
        product_id = item['product_id']
        size = item['size']
        product = Product.objects.get(pk = product_id)
        user = request.user
        new_item = Cart.objects.create(user=user, product=product, size=size)
    logout(request)
    return redirect('index')


# register view
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def register(request):
    if request.method == 'POST':
        # gets the filled registration form that's in the html
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            # cleaned_data makes sure it doesn't have thing that could be harmful
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')

        # if input is invalid
        else:
            context = {
                'form': RegisterationForm(),
                'error': "please fill the requirements"
            }
            return render(request, 'myshop/register.html', context)

    # if request method is get, sends an non-filled regestration form
    else:
        form = RegisterationForm()

        context = {
            'form': form
        }
        return render(request, 'myshop/register.html', context)


def women_tops(request):
    context = {
        "title": "Women's Tops",
        "category": "Tops",
        "gender": "Women's",
        "products": Product.objects.filter(category="Top", gender="Female", available=True)
    }
    return render(request, "myshop/products.html", context)


def women_bottoms(request):
    context = {
        "title": "Women's Bottoms",
        "category": "Bottoms",
        "gender": "Women's",
        "products": Product.objects.filter(category="Bottom", gender="Female", available=True)
    }
    return render(request, "myshop/products.html", context)


def dresses(request):
    context = {
        "title": "Dresses",
        "category": "Dresses",
        "gender": "Women's",
        "products": Product.objects.filter(category="Dress", gender="Female", available=True)
    }
    return render(request, "myshop/products.html", context)


def women_shoes(request):
    context = {
        "title": "Women's Shoes",
        "category": "Shoes",
        "gender": "Women's",
        "products": Product.objects.filter(category="Shoes", gender="Female", available=True)
    }
    return render(request, "myshop/products.html", context)


def women_activewear(request):
    context = {
        "title": "Women's Activewear",
        "category": "Activewear",
        "gender": "Women's",
        "products": Product.objects.filter(category="Activewear", gender="Female", available=True)
    }
    return render(request, "myshop/products.html", context)


def men_tops(request):
    context = {
        "title": "Men's Tops",
        "category": "Tops",
        "gender": "Men's",
        "products": Product.objects.filter(category="Top", gender="Male", available=True)
    }
    return render(request, "myshop/products.html", context)


def men_bottoms(request):
    context = {
        "title": "Men's Bottoms",
        "category": "Bottoms",
        "gender": "Men's",
        "products": Product.objects.filter(category="Bottom", gender="Male", available=True)
    }
    return render(request, "myshop/products.html", context)


def men_shoes(request):
    context = {
        "title": "Men's Shoes",
        "category": "Shoes",
        "gender": "Men's",
        "products": Product.objects.filter(category="Shoes", gender="Male", available=True)
    }
    return render(request, "myshop/products.html", context)


def men_activewear(request):
    context = {
        "title": "Men's Activewear",
        "category": "Activewear",
        "gender": "Men's",
        "products": Product.objects.filter(category="Activewear", gender="Male", available=True)
    }
    return render(request, "myshop/products.html", context)


def product(request, product_id):
    product = Product.objects.get(pk = product_id)
    sizes = product.sizes
    sizes = sizes.split() # https://stackoverflow.com/questions/19555472/change-a-string-of-integers-separated-by-spaces-to-a-list-of-int
    context = {
        "product": product,
        "sizes": sizes,
        "comments": product.comments.all()
    }
    return render(request, "myshop/product.html", context)


def comment(request, product_id):
    text = request.POST['comment']
    product = Product.objects.get(pk = product_id)
    user = request.user
    comment = Comment.objects.create(user=user, product=product, text=text)
    return HttpResponseRedirect(reverse('product', args=[product_id]))


# https://groups.google.com/forum/#!topic/django-users/8uW5jDP3Fgw
def add_to_cart(request, product_id):
    size = request.POST['size']
    cart = request.session.get('cart', [])
    cart.append({'product_id': product_id, 'size': size})
    request.session['cart']=cart
    return HttpResponseRedirect(reverse('product', args=[product_id]))


def cart(request):
    if request.user.is_authenticated:
        try:
            cart = request.session.get('cart', [])
            user = request.user
            for item in cart:
                product_id = item['product_id']
                size = item['size']
                product = Product.objects.get(pk = product_id)
                new_item = Cart.objects.create(user=user, product=product, size=size)
            del request.session['cart']
        except KeyError:
            items = Cart.objects.filter(user=user).values()

        items = Cart.objects.filter(user=user).values()
    else:
        items = request.session.get('cart', [])

    products=[]
    for item in items:
        product_id = item['product_id']
        size = item['size']
        product = Product.objects.get(pk = product_id)
        products.append({'product': product, 'size': size})
    context = {
        "products": products
    }
    return render(request, 'myshop/cart.html', context)