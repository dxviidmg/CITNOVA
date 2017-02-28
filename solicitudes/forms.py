from .models import *
from accounts.models import Departamento
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import Select
from django.contrib import admin

class SolicitudRecursoFinancieroCreateForm(forms.ModelForm):


	class Meta:
		model = SolicitudRecursoFinanciero
		exclude = ('folio', )

	def __init__(self, departamento=None, **kwargs):
		super(SolicitudRecursoFinancieroCreateForm, self).__init__(**kwargs)
		if departamento:
			self.fields['a_nombre_de'].queryset = User.objects.filter(departamento=departamento).order_by('first_name', 'last_name')