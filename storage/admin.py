from django.contrib import admin
from storage.models import Product, Package

# Register your models here.


class Products(admin.ModelAdmin):
    list_display = ('id', 'product_name',
                    'product_buy_price', 'product_sell_price')
    list_display_links = ('product_name',
                          'product_buy_price', 'product_sell_price')
    search_fields = ('id', 'product_name')
    list_per_page = 25


admin.site.register(Product, Products)


class Packages(admin.ModelAdmin):
    list_display = ('id', 'product', 'package_buy_price', 'package_sell_price', 'package_amount', 'stock_amount')
    list_display_links = ('package_buy_price', 'package_sell_price', 'package_amount', 'stock_amount')
    search_fields = ('id', 'product')
    list_per_page = 25

admin.site.register(Package, Packages)
