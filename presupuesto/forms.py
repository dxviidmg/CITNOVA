from django import forms
from .models import *
from decimal import Decimal

class MesCreateForm(forms.ModelForm):
	class Meta:
		model = Mes
		fields = ( 'mes','monto_autorizado',)

class MesEditForm(forms.ModelForm):
	class Meta:
		model = Mes
		fields = ( 'monto_ampliacion','monto_reduccion', 'monto_ejercido',)

class PartidaCreateForm(forms.ModelForm):
	class Meta:
		model = Partida
		fields = ( 'codigo','descripcion',)

class CapituloCreateForm(forms.ModelForm):
	class Meta:
		model = Capitulo
		fields = ( 'codigo',)

class ModificacionForm(forms.Form):
	cantidad = forms.DecimalField(max_digits=20,decimal_places=2)

	def clean(self):
		cd = self.cleaned_data
		return cd