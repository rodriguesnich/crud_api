from rest_framework import viewsets
from storage.models import Package, Product
from storage.serializers import PackageSerializer, ProductSerializer, StockSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """Return all Products"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PackageViewSet(viewsets.ModelViewSet):
    """Return all Packages With Products"""
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class StockViewSet(viewsets.ModelViewSet):
    """Return Stock Infos"""
    queryset = Package.objects.all()
    serializer_class = StockSerializer
