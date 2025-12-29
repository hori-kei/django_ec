# cart/urls.py
from django.urls import path

from .views import AddToCartView, CartDetailView

app_name = "cart"

urlpatterns = [
    path("", CartDetailView.as_view(), name="detail"),
    path("add/<int:product_id>/", AddToCartView.as_view(), name="add"),
]
