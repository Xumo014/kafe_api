from django.contrib import admin
from products.models import Cafe, CategoryEat, Category, Product
# Register your models here.

admin.site.register(Cafe)
admin.site.register(CategoryEat)
admin.site.register(Category)
admin.site.register(Product)
