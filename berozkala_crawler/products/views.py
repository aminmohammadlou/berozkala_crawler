from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'category'
    lookup_url_kwarg = 'category'

    
class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
