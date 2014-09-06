from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html') #context is 3rd param


def about(request):
    return render(request, 'home/about.html') #context is 3rd param
