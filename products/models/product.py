# from django.contrib.gis.db.models import PointField
from django.db import models


class Cafe(models.Model):
    name = models.CharField(max_length=100)
    extended_name = models.CharField(max_length=255,blank=True, null=True)
    address = models.TextField()
    owner = models.CharField(max_length=100) #rahbar
    manager = models.CharField(max_length=100) #boshqaruvchi
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    telegram_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    # location = PointField(geography=True, blank=True, null=True) #aniq geografik koorfinatalar olish uchun (long, lat)
    image = models.ImageField(upload_to="products/cafes/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name



class CategoryEat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    composition = models.TextField() # tarkibi
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='media/products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    categoryeat = models.ForeignKey(CategoryEat, on_delete=models.SET_NULL, null=True, blank=True)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


