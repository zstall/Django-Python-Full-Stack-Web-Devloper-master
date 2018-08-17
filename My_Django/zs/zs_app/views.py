from django.shortcuts import render

# Create your views here.
def index(request):
    zs_dict = {'insert_content': "Zachary Stall"}
    return render(request, 'zs_app/index.html', context=zs_dict)
