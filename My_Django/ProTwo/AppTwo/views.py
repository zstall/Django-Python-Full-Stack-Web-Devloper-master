from django.shortcuts import render
from AppTwo.models import User
# Create your views here.
def index(request):
    return render(request,'AppTwo/index.html')

def users(request):
    user_list = User.objects.order_by('last_name')
    user_dict = {"users":user_list}
    return render(request,'AppTwo/users.html', context=user_dict)
