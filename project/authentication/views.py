from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe

from django.contrib.auth import logout

from . import forms

@require_safe
def login(request):
    logout(request)

    loginForm = forms.LoginForm()
    context = {
        'form': loginForm,
    }

    return render(request, 'auth/login.html', context)

@require_safe
def cadastro(request):
    cadastroForm = forms.CadastroForm()
    context = {
        'form': cadastroForm,
    }
    return render(request, 'auth/cadastro.html', context)