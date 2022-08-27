from rest_framework.viewsets import ModelViewSet
#import django_filters.rest_framework
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_fields = ['title']
    # search_fields = ['title', 'description']
    pagination_class = LimitOffsetPagination

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['products']
    pagination_class = LimitOffsetPagination