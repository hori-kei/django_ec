# cart/views.py
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from product.models import Product

from .models import CartItem
from .utils import get_or_create_cart


class AddToCartView(View):
    def post(self, request, product_id):
        cart = get_or_create_cart(request)
        product = get_object_or_404(Product, pk=product_id)

        quantity = request.POST.get("quantity", "1")
        try:
            quantity = int(quantity)
        except ValueError:
            quantity = 1
        if quantity < 1:
            quantity = 1

        cart_item, _created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()

        return redirect("cart:detail")


class CartDetailView(TemplateView):
    template_name = "cart/cart_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = get_or_create_cart(self.request)
        context["cart_items"] = CartItem.objects.filter(cart=cart).select_related("product")
        return context


class RemoveCartView(View):
    def post(self, request, item_id):
        cart = get_or_create_cart(request)

        # 自分のカートの item しか削除できないようにする
        cart_item = get_object_or_404(CartItem, pk=item_id, cart=cart)
        cart_item.delete()

        return redirect("cart:detail")
