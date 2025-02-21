from django_filters import rest_framework as django_filters
from products.models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category', 'categoryeat', 'cafe']