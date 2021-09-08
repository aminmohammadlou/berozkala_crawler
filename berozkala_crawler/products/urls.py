from django.urls import path
from .views import CategoryListAPIView, ProductListAPIView, ProductDetailAPIView

app_name = 'products'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<str:category>/', ProductListAPIView.as_view(), name='product_list'),
    path('categories/<str:category>/<str:name>/', ProductDetailAPIView.as_view(), name='product_detail'),
]