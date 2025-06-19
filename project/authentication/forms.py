from django.forms import ModelForm
from . import models

class LoginForm(ModelForm):
    class Meta:
        model = models.CustomUser
        fields = ["username", "password"]

class CadastroForm(ModelForm):
    class Meta:
        model = models.CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "address",
        ]

