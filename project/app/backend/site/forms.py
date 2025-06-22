from django import forms

class FormExemplo(forms.Form):
    campo1 = forms.CharField()
    campo2 = forms.CharField()
    campo3 = forms.CharField()