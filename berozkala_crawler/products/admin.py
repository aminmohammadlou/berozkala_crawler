from django.contrib import admin

from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_time', 'updated_time')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('category',)
    list_display = ('name', 'price', 'category')