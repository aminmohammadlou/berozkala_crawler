from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)
    url = models.URLField(verbose_name='URL', blank=False)
    created_time = models.DateTimeField('Created Time', auto_now_add=True)
    updated_time = models.DateTimeField('Updated Time', auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_list', kwargs={'category': self.name})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)
    price = models.IntegerField(verbose_name='Price', help_text="In Tuman")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    created_time = models.DateTimeField('Created Time', auto_now_add=True)
    updated_time = models.DateTimeField('Updated Time', auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'product': self.pk})

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'