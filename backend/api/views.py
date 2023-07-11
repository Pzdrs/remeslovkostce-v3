from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from remeslovkostce.models import Product, ProductCategory
from remeslovkostce.serializers import ProductSerializer, ProductCategorySerializer, ProductDetailSerializer


# Create your views here.

class HomeView(APIView):
    def get(self, request, format=None):
        return Response({
            'success': True,
        })


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryListView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
