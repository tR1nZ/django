from distutils.command.upload import upload
from email.mime import image
from pydoc import describe
from statistics import quantiles
from unicodedata import category
from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=512)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    description = models.CharField(max_length=512)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Продукт: {self.name} | Категории: {self.category.name}'