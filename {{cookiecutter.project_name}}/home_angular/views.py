from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home_angular/index.html') #context is 3rd param