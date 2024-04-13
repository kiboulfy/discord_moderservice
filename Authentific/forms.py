from django import forms 
from django.forms import ModelForm
from .models import Adding

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

class AddingForm(ModelForm):
    class Meta:
        model = Adding
        fields = '__all__'

class AddingChangeFoem(forms.Form):
    pass