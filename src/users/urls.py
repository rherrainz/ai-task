from . import views
from django.urls import path

urlpatterns = [
    path('users/', views.UserView.get_all_users, name='user_list'),
    path('users/<int:user_id>/', views.UserView.get_user_by_id, name='user_detail'),
]