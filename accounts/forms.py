from django import forms
from django.contrib.auth.models import User
from .models import *

#Formularios de empleado
class UserEmpleadoCreateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'departamento',)

class PerfilEmpleadoCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('grado_profesional', 'puesto', 'teléfono', 'banco', 'cuenta_bancaria', 'CLABE')

#formularios de director
class UserDirectorCreateForm(forms.ModelForm):
	password = forms.CharField(label='Password',widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repite tu password',widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username','first_name', 'last_name', 'email', 'departamento')
	
	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Los passwords no coicinden')
		return cd['password2']

	def clean_username(self):
	    username = self.cleaned_data['username']
	    try:
	        user = User.objects.exclude(pk=self.instance.pk).get(username=username)
	    except User.DoesNotExist:
	        return username
	    raise forms.ValidationError(u'Username "%s" is already in use.' % username)

class UserDirectorEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'departamento')

class PerfilDirectorCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('grado_profesional', 'teléfono', 'banco', 'cuenta_bancaria', 'CLABE')




#Formularios de proveedor
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