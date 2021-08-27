from django.db import models
from django.db.models.fields import CharField, IntegerField, URLField
from django.db.models.fields.related import ForeignKey

class Category(models.Model):
    name = CharField(verbose_name='Name', max_length=200)
    url = URLField()

class Product(models.Model):
    name = CharField(verbose_name='Name', max_length=200)
    price = IntegerField(verbose_name='Price', help_text="In Tuman")
    category = ForeignKey(Category, on_delete=models.CASCADE)
