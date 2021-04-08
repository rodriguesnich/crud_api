from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_buy_price = models.DecimalField(max_digits=100, decimal_places=2)
    product_sell_price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.product_name

class Package(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.SET_NULL, null=True)
    package_buy_price = models.DecimalField(max_digits=100, decimal_places=2)
    package_sell_price = models.DecimalField(max_digits=100, decimal_places=2)
    package_amount = models.IntegerField(null=True)
    stock_amount = models.IntegerField(null=True)