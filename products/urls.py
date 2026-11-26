from django.urls import path
from . import views

urlpatterns = [

     path('category/', views.productsPage, name='category' ),

     path('product/', views.product_page, name='product_page'),

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'upload/',
        views.upload_product,
        name='upload_product'
    ),

    path(
        'add-to-cart/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        views.cart_view,
        name='cart'
    ),

    path(
        'remove-from-cart/<int:product_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),

]