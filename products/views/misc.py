from rest_framework import viewsets
from products.models import Category, CategoryEat, Cafe
from products.serializers import CategorySerializer, CategoryEatSerializer, CafeSerializer


class CafeViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

class CategoryEatViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = CategoryEat.objects.all()
    serializer_class = CategoryEatSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
