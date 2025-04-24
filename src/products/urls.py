from .views import ProductView, ProductDetailView
from django.urls import path

urlpatterns = [
    path('products/', ProductView.as_view(), name='user_list'),
    path('users/<int:user_id>/', ProductDetailView.as_view(), name='user_detail'),
]