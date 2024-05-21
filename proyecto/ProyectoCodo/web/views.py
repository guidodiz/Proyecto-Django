from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.shortcuts import redirect

def index(request):
    return render(request, 'web/index.html')

def profile(request, name):
    context={
        'nombre': name
    }

    return render(request, 'web/profile.html', context)

def books(request):
    context={
        'libro1':{'titulo':'kimetsu no yaiba', 'autor': 'aaa', 'año':2019},
        'libro2':{'titulo':'hunterxhunter', 'autor': 'aaa', 'año':2011}
    }

    return render(request, 'web/books.html', {'books':context})

def rent(request):
    context={}

    if request.method == "GET":
        context ['form'] = Alquiler()
    else:
        context ['form'] = Alquiler(request.POST)
        return redirect('index')
    
    return render(request, 'web/rent.html', context)