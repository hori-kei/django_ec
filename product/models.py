# Create your models here.
from django.db import models


class Product(models.Model):
    class Meta:
        db_table = "product"

    name = models.CharField("商品名", max_length=100)
    price = models.IntegerField("価格", default=0)
    image = models.CharField("画像", max_length=255)
    created_at = models.DateTimeField("掲載日", auto_now_add=True)

    def __str__(self):
        return self.name
