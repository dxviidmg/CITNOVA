from .models import *
from accounts.models import Departamento
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import Select
from django.contrib import admin

class SolicitudRecursoFinancieroCreateForm(forms.ModelForm):

	class Meta:
		model = SolicitudRecursoFinanciero
		fields = ('a_nombre_de', 'concepto', 'importe_numero', 'importe_letra', 'metodo_pago')

	def __init__(self, departamento=None, **kwargs):
		super(SolicitudRecursoFinancieroCreateForm, self).__init__(**kwargs)
		if departamento:
			self.fields['a_nombre_de'].queryset = User.objects.filter(is_active=True, departamento=departamento).order_by('first_name', 'last_name')

class SolicitudRecursoFinancieroCreateForm2(forms.ModelForm):

	class Meta:
		model = SolicitudRecursoFinanciero
		fields = ('a_nombre_de', 'concepto', 'importe_numero', 'importe_letra', 'metodo_pago')

	def __init__(self, *args, **kwargs):
		super(SolicitudRecursoFinancieroCreateForm2, self).__init__(**kwargs)
		self.fields['a_nombre_de'].queryset = User.objects.filter(is_active=True, departamento__isnull=True, is_staff=False).order_by('first_name', 'last_name')