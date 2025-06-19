from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseForbidden

from django.contrib.auth import logout
from authentication import api

from . import forms

@require_http_methods(['GET','POST'])
def login(request):

    if request.method == 'POST':
        loginForm = forms.LoginForm(request.POST)
        response = api.LoginApi(request, loginForm)

        
    elif request.method == 'GET':
        logout(request)
        loginForm = forms.LoginForm()
        context = {
            'form': loginForm,
        }
        
        response = render(request, 'auth/login.html', context)

    else:
        response = HttpResponseForbidden('Não era pra você chegar aqui nem por milagre, pilantrinha...')


    return response

@require_http_methods(['GET','POST'])
def cadastro(request):
    cadastroForm = forms.CadastroForm()
    context = {
        'form': cadastroForm,
    }
    return render(request, 'auth/cadastro.html', context)