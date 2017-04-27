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
		fields = ('grado_profesional', 'puesto', 'teléfono', 'banco', 'cuenta_bancaria', 'CLABE')

class UserProveedorCreateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class PerfilProveedorCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('grado_profesional', 'teléfono', 'banco', 'cuenta_bancaria', 'CLABE')

class ExpedienteProveedorCreateForm(forms.ModelForm):
	class Meta:
		model = Expediente
#		fields = ('tipo', 'RFC', 'IFE')
		fields = ('tipo', 'Identifación_oficial', 'RFC', 'Comprobante_de_domicilio', 'Registro_de_padrón_de_proveedores', 'Tres_cotizaciones', 'Opinión_de_cumplimiento', 'Acta_constitutiva', 'Representación_legal')

class UserDesactivateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('is_active',)