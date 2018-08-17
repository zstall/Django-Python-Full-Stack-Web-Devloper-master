from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<strong>Demo of linking views to urls</strong>")

def zsAppProj(request):
    # helpdict = {'help_insert':"Help Page"}
    return render(request, 'zsAppProj/zsAppProj.html', context='')
