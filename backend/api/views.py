from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from remeslovkostce.models import Product, ProductCategory
from remeslovkostce.serializers import ProductSerializer, ProductCategorySerializer


# Create your views here.

class HomeView(APIView):
    def get(self, request, format=None):
        return Response("Hello, world!")


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryListView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
