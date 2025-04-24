from .views import UserDetailView, UserView
from django.urls import path

urlpatterns = [
    path('users/', UserView.as_view(), name='user_list'),
    path('users/<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
]