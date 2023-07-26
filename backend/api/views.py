from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from remeslovkostce.models import Product, ProductCategory
from remeslovkostce.serializers import \
    ProductSerializer, \
    ProductCategorySerializer, \
    ProductDetailSerializer


# Create your views here.

class HomeView(APIView):
    """
    View to confirm that the API is working.
    """

    def get(self, request, format=None):  # pylint: disable=unused-argument,redefined-builtin,missing-function-docstring
        return Response({
            'success': True,
        })


class ProductListView(ListAPIView):
    """
    View to list all users in the system.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryListView(ListAPIView):
    """
    View to list all categories in the system.
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductDetailView(RetrieveAPIView):
    """
    View with detailed information about a certain product
    """
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
