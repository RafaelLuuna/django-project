from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect 
from django.views.decorators.http import require_POST

from django.contrib.auth import authenticate, login, logout
from authentication.models import ROLES
from django.conf import settings

@require_POST
def LoginApi(request, form):
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
    User = authenticate(
        username=username,
        password=password
    )
    
    if User is not None:
        login(request, User)
        redirectUrl = ROLES[User.role]['default_page']
        return HttpResponseRedirect(redirectUrl)

    # Por padrão, caso a API não consiga encontrar o usuário, ela incluirá um erro no formulário e renderizará a view de login
    form.add_error(None, 'Não foi possível realizar o login')
    context = {
        'form': form,
    }
    return render(request, 'auth/login.html', context)
    

@require_POST
def LogoutApi(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

@require_POST
def SingupApi():
    pass