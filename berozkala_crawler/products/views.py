from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'category'
    lookup_url_kwarg = 'category'

    def get_queryset(self):
        queryset = Product.objects.filter(category__name=self.kwargs['category'])
        return queryset

    
class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'    
