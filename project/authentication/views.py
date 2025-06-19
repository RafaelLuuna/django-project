from django.shortcuts import render
from . import forms

def login(request):
    loginForm = forms.LoginForm()
    context = {
        'form': loginForm,
    }
    return render(request, 'auth/login.html', context)


def cadastro(request):
    cadastroForm = forms.CadastroForm()
    context = {
        'form': cadastroForm,
    }
    return render(request, 'auth/cadastro.html', context)