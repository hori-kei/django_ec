from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = "商品データを登録します"

    def handle(self, *args, **options):
        products = [
            {"name": "Tシャツ", "price": 1500, "image": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg"},
            {"name": "スニーカー", "price": 8000, "image": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg"},
            {"name": "バッグ", "price": 5200, "image": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg"},
            {"name": "ジャケット", "price": 12000, "image": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg"},
        ]

        for p in products:
            Product.objects.get_or_create(**p)

        self.stdout.write(self.style.SUCCESS("商品データを登録しました！"))
