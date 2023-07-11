from django.urls import path

from api.views import HomeView, ProductListView, ProductCategoryListView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('products/', ProductListView.as_view(), name="product-list"),
    path('categories/', ProductCategoryListView.as_view(), name="product-list"),
]
