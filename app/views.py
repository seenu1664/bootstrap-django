from django.shortcuts import render

# Create your views here.

def bootstrap(request):
    return render(request,'bootstrap.html')

def background(request):
    return render (request,'background.html')