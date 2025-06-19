from django.shortcuts import render, redirect

def index(request):
    return redirect('login/')

def home(request):
    return render(request, 'site/home.html')
