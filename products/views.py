from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Product


class ProductListView(ListView):
    template_name = "products/list.html"
    model = Product


class ProductDetailView(DetailView):
    template_name = "detail/detail.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_product = self.object

        # 1. 現在の商品IDを除外 (exclude)
        # 2. 作成日時で降順に並び替え (order_by('-created_at'))
        # 3. 最初の4件を取得 ([:4])
        related_product = self.model.objects.exclude(pk=current_product.pk).order_by("-created_at")[
            :4
        ]

        context["related_products"] = related_product
        return context
