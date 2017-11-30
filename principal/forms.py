#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from principal.models import *

class LogInForm(forms.Form):
    user = forms.CharField(label="Usuario", widget=forms.TextInput, required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)

class AlumnoForm(ModelForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput, required=True)
    user = forms.CharField(label="Usuario", widget=forms.TextInput, required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Repita Password", widget=forms.PasswordInput, required=True)
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellidos', 'universidad', 'titulacion']
        
class ProfesorForm(ModelForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput, required=True)
    user = forms.CharField(label="Usuario", widget=forms.TextInput, required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellidos', 'universidad', 'departamento']

class TFGForm(ModelForm):
    class Meta:
        model = TFG
        
class SearchForm(forms.Form):
    titulacion = forms.CharField(label='TItulación', widget=forms.TextInput, required=True)
