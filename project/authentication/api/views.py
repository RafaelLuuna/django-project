from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.views.decorators.http import require_POST

from django.contrib.auth import authenticate, login, logout
from authentication.models import ROLES
from django.conf import settings

@require_POST
def LoginApi(request):
    username = request.POST['username'] if 'username' in request.POST else ''
    password = request.POST['password'] if 'password' in request.POST else ''
    User = authenticate(
        username=username,
        password=password
    )
    if User is not None:
        login(request, User)
        redirectUrl = ROLES[User.role]['default_page']
        return HttpResponseRedirect(redirectUrl)

    return redirect(settings.LOGIN_URL)
    

@require_POST
def LogoutApi(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

@require_POST
def SingupApi():
    pass