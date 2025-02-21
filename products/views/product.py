from rest_framework import viewsets, filters

from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as django_filters
from products.filters import ProductFilter


class CustomPagination(PageNumberPagination):
    page_size = 5
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    pagination_class = CustomPagination
    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
