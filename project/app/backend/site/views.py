from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import forms

@login_required
def index(request):
    return redirect('/home/')


@login_required
def home(request):
    context = {}
    return render(request, 'site/home.html', context)



@login_required
def formulario_exemplo(request):
    form = forms.FormExemplo
    context = {
        'form': form
    }
    return render(request, 'site/formulario_exemplo.html', context)


@login_required
def tabela_exemplo(request):
    # Dados fake (não está conectado com o banco de dados)
    context = {
        'contents': [
            {
                'nome': 'Rafael',
                'email': 'rafael@email.com',
                'funcao': 'front-end',
            },
            {
                'nome': 'Lucas',
                'email': 'lucas@email.com',
                'funcao': 'infra',
            },
            {
                'nome': 'Arthur',
                'email': 'arthur@email.com',
                'funcao': 'back-end',
            },
        ]

    }
    return render(request, 'site/tabela_exemplo.html', context)
