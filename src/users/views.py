from django.views.generic import ListView, DetailView
from . import models

class UserView(ListView):
    model = models.User
    template_name = 'views/user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = models.User
    template_name = 'views/user_detail.html'
    context_object_name = 'user'