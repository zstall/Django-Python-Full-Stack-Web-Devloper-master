from django.shortcuts import render

# Create your views here.
def help(request):
    helpdict = {'help_insert':"Help Page"}
    return render(request, 'help/help.html', context=helpdict)
