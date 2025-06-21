from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return redirect('/home/')

@login_required
def home(request):
    return render(request, 'site/home.html')
