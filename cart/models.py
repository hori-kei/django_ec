from django.db import models

from product.models import Product


class Cart(models.Model):
    session_key = models.CharField("セッションキー", max_length=40, unique=True)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)

    def __str__(self):
        return f"Cart({self.session_key})"


class CartItem(models.Model):
    class Meta:
        db_table = "cart_items"
        constraints = [
            models.UniqueConstraint(
                fields=["cart", "product"],
                name="uniq_cart_product",
            )
        ]

    cart = models.ForeignKey(
        Cart,
        verbose_name="カート",
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(
        Product,
        verbose_name="商品",
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField("個数", default=0)

    def __str__(self):
        return f"CartItem(cart={self.cart_id}, product={self.product_id}, qty={self.quantity})"

    @property
    def subtotal(self):
        return self.product.price * self.quantity
