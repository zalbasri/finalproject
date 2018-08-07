from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path('logout', views.logout_view, name='logout'),
    path("register", views.register, name="register"),
    path('women_tops', views.women_tops, name='women_tops'),
    path('women_bottoms', views.women_bottoms, name='women_bottoms'),
    path('dresses', views.dresses, name='dresses'),
    path('women_shoes', views.women_shoes, name='women_shoes'),
    path('women_activewear', views.women_activewear, name='women_activewear'),
    path('men_tops', views.men_tops, name='men_tops'),
    path('men_bottoms', views.men_bottoms, name='men_bottoms'),
    path('men_shoes', views.men_shoes, name='men_shoes'),
    path('men_activewear', views.men_activewear, name='men_activewear'),
    path("<int:product_id>", views.product, name="product"),
    ]