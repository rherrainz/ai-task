from .views import ProductView, ProductDetailView
from django.urls import path

urlpatterns = [
    path('products/', ProductView.as_view(), name='product_list'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
]