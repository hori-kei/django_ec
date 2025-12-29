# cart/views.py
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from product.models import Product

from .models import CartItem
from .utils import get_or_create_cart


class AddToCartView(View):
    def post(self, request, product_id):
        cart = get_or_create_cart(request)
        product = get_object_or_404(Product, pk=product_id)

        cart_item, _created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()

        return redirect("product:product_list")
