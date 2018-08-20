from django.shortcuts import render
from user_app.models import User, Username, Email

# Create your views here.
def user_app(request):
    user_list = Email.objects.order_by('person')
    email_dict = {'acc_records':user_list}
    return render(request,'user_app/user_app.html',context=email_dict)
