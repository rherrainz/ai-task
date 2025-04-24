from django.shortcuts import render
from .models import User
# Create your views here.
class UserView:
    def get_all_users(request):
        users = User.objects.all()
        return render(request, 'users/user_list.html', {'users': users})
    
    def get_user_by_id(request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'users/user_detail.html', {'user': user})

