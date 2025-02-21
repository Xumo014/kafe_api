from rest_framework import serializers
from products.models import Cafe, CategoryEat, Category, Product


class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = '__all__'

class CategoryEatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryEat
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'