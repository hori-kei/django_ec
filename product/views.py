from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.order_by("-created_at")


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"
    context_object_name = "product"
