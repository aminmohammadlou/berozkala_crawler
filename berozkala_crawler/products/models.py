from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200, primary_key=True)
    url = models.URLField(verbose_name='URL', unique=True, blank=False)
    created_time = models.DateTimeField('Created Time', auto_now_add=True)
    updated_time = models.DateTimeField('Updated Time', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200, primary_key=True)
    price = models.IntegerField(verbose_name='Price', help_text="In Tuman")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_time = models.DateTimeField('Created Time', auto_now_add=True)
    updated_time = models.DateTimeField('Updated Time', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'