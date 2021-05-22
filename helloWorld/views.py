from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {
        'sample_text' : "Hello I am from hello world view !"
    }
    return render(request, 'index.html', context = my_dict)

