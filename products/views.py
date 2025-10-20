from django.shortcuts import render
from django.views import View


class ProductListView(View):
    def get(self, request):
        # 後でここでDBから商品一覧を取得する
        return render(request, "products/list.html")
