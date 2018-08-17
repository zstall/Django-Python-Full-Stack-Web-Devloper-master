from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<em>My Second Projecct</em>")

def help(request):
    helpdict = {'help_insert': 'Help Page'}
    return render(request, 'AppTwo/help.html', context=helpdict)

def user(request):
    return render(request, 'user/user.html', context='')
