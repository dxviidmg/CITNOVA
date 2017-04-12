from django import forms
from django.contrib.auth.models import User
from .models import *

class UserEmpleadoCreateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'departamento',)

class PerfilEmpleadoCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('grado_profesional', 'puesto', 'telefono', 'banco', 'cuenta_bancaria', 'CLABE')

class UserProveedorCreateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class PerfilProveedorCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('grado_profesional', 'telefono', 'banco', 'cuenta_bancaria', 'CLABE')

class ExpedienteProveedorCreateForm(forms.ModelForm):
	class Meta:
		model = Expediente
		fields = ('tipo', 'RFC', 'IFE')