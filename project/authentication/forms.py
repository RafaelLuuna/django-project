from django import forms
from . import models

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class CadastroForm(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
        ]

