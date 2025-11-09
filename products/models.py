from django.db import models


class Product(models.Model):
    class Meta:
        db_table = "product"

    name = models.CharField(verbose_name="商品名", max_length=100)
    price = models.IntegerField(verbose_name="価格")
    image = models.ImageField(
        verbose_name="商品画像URL",
        upload_to="products/",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
