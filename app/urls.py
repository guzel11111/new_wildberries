from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<slug:product_slug>/", views.product_details,
         name="product_details"),
    path("cart/", views.cart_view, name="cart"),  # <-- вот это обязательно
    path("add-to-cart/<slug:product_slug>/", views.add_to_cart, name="add_to_cart"),
    path("remove-from-cart/<slug:product_slug>/", views.remove_from_cart, name="remove_from_cart"),
]