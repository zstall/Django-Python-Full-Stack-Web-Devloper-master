from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index_app/index_app.html', context='')

def index_app(request):
    return render(request, 'index_app/index_app.html', context='')
