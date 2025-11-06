from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
    template_name = "products/list.html"
    model = Product
    
