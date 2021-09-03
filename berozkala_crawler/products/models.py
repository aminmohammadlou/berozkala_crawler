from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200, primary_key=True)
    url = models.URLField()

class Product(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200, primary_key=True)
    price = models.IntegerField(verbose_name='Price', help_text="In Tuman")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
