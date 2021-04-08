from rest_framework import serializers
from storage.models import Product, Package


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name',
                  'product_buy_price', 'product_sell_price']


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        # fields = '__all__'
        exclude = ['stock_amount']
        depth = 1


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        # fields = '__all__'
        exclude = ['package_amount']
        depth = 1
