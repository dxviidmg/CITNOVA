from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from django.db.models import Sum
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import *
from django.contrib import messages
from decimal import Decimal
from django.contrib import messages
import datetime

class ListViewProgramas(View):
	def get(self, request):
		template_name = "presupuesto/listProgramas.html"
		hoy = datetime.datetime.now()
		programas = Programa.objects.filter(año=hoy.year).order_by('nombre')
		context = {
		'programas': programas,
		}
		return render(request, template_name, context)

class ListViewCapitulos(View):
	def get(self, request, pk):
		template_name = "presupuesto/listCapitulos.html"
		programa = get_object_or_404(Programa, pk=pk)
		capitulos = Capitulo.objects.filter(programa=programa).order_by('codigo')

		total_monto_anual_autorizado_dict = Capitulo.objects.filter(programa=programa).aggregate(Sum('monto_anual_autorizado'))
		total_monto_anual_autorizado = total_monto_anual_autorizado_dict['monto_anual_autorizado__sum']

		total_monto_anual_ampliacion_dict = Capitulo.objects.filter(programa=programa).aggregate(Sum('monto_anual_ampliacion'))
		total_monto_anual_ampliacion = total_monto_anual_ampliacion_dict['monto_anual_ampliacion__sum']		

		total_monto_anual_reduccion_dict = Capitulo.objects.filter(programa=programa).aggregate(Sum('monto_anual_reduccion'))
		total_monto_anual_reduccion = total_monto_anual_reduccion_dict['monto_anual_reduccion__sum']

		total_monto_anual_modificado_dict = Capitulo.objects.filter(programa=programa).aggregate(Sum('monto_anual_modificado'))
		total_monto_anual_modificado = total_monto_anual_modificado_dict['monto_anual_modificado__sum']

		total_monto_anual_ejercido_dict = Capitulo.objects.filter(programa=programa).aggregate(Sum('monto_anual_ejercido'))
		total_monto_anual_ejercido = total_monto_anual_ejercido_dict['monto_anual_ejercido__sum']

		total_monto_anual_por_ejercer_dict = Capitulo.objects.filter(programa=programa).aggregate(Sum('monto_anual_por_ejercer'))
		total_monto_anual_por_ejercer = total_monto_anual_por_ejercer_dict['monto_anual_por_ejercer__sum']

		context = {
		'programa': programa,
		'capitulos': capitulos,
		'total_monto_anual_autorizado': total_monto_anual_autorizado,
		'total_monto_anual_ampliacion': total_monto_anual_ampliacion,
		'total_monto_anual_reduccion': total_monto_anual_reduccion,
		'total_monto_anual_modificado': total_monto_anual_modificado,
		'total_monto_anual_ejercido': total_monto_anual_ejercido,
		'total_monto_anual_por_ejercer': total_monto_anual_por_ejercer,
		}
		return render(request, template_name, context)

class ListViewPartidas(View):
	def get(self, request, pk):
		template_name = "presupuesto/listPartidas.html"
		capitulo = get_object_or_404(Capitulo, pk=pk)
		partidas = Partida.objects.filter(capitulo=capitulo).order_by('codigo')
		programa = Programa.objects.get(capitulo=capitulo)
		
		total_monto_anual_autorizado_dict = Partida.objects.filter(capitulo=capitulo).aggregate(Sum('monto_anual_autorizado'))
		total_monto_anual_autorizado = total_monto_anual_autorizado_dict['monto_anual_autorizado__sum']
		
		total_monto_anual_ampliacion_dict = Partida.objects.filter(capitulo=capitulo).aggregate(Sum('monto_anual_ampliacion'))
		total_monto_anual_ampliacion = total_monto_anual_ampliacion_dict['monto_anual_ampliacion__sum']

		total_monto_anual_reduccion_dict = Partida.objects.filter(capitulo=capitulo).aggregate(Sum('monto_anual_reduccion'))
		total_monto_anual_reduccion = total_monto_anual_reduccion_dict['monto_anual_reduccion__sum']

		total_monto_anual_modificado_dict = Partida.objects.filter(capitulo=capitulo).aggregate(Sum('monto_anual_modificado'))
		total_monto_anual_modificado = total_monto_anual_modificado_dict['monto_anual_modificado__sum']

		total_monto_anual_ejercido_dict = Partida.objects.filter(capitulo=capitulo).aggregate(Sum('monto_anual_ejercido'))
		total_monto_anual_ejercido = total_monto_anual_ejercido_dict['monto_anual_ejercido__sum']
		
		total_monto_anual_por_ejercer_dict = Partida.objects.filter(capitulo=capitulo).aggregate(Sum('monto_anual_por_ejercer'))
		total_monto_anual_por_ejercer = total_monto_anual_por_ejercer_dict['monto_anual_por_ejercer__sum']

		context = {
		'capitulo': capitulo,
		'partidas': partidas,
		'programa': programa,
		'total_monto_anual_autorizado': total_monto_anual_autorizado,
		'total_monto_anual_ampliacion': total_monto_anual_ampliacion,
		'total_monto_anual_reduccion': total_monto_anual_reduccion,
		'total_monto_anual_modificado': total_monto_anual_modificado,
		'total_monto_anual_ejercido': total_monto_anual_ejercido,
		'total_monto_anual_por_ejercer': total_monto_anual_por_ejercer,
		}
		return render(request, template_name, context)

class ListViewMeses(View):
	def get(self, request, pk):
		template_name = "presupuesto/listMeses.html"
		partida = get_object_or_404(Partida, pk=pk)
		meses = Mes.objects.filter(partida=partida).order_by('mes')
		capitulo = Capitulo.objects.get(partida=partida)
		programa = Programa.objects.get(capitulo=capitulo)
		
		total_monto_autorizado_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_autorizado'))
		total_monto_autorizado = total_monto_autorizado_dict['monto_autorizado__sum']

		total_monto_ampliacion_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_ampliacion'))
		total_monto_ampliacion = total_monto_ampliacion_dict['monto_ampliacion__sum']

		total_monto_reduccion_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_reduccion'))
		total_monto_reduccion = total_monto_reduccion_dict['monto_reduccion__sum']

		total_monto_modificado_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_modificado'))
		total_monto_modificado = total_monto_modificado_dict['monto_modificado__sum']

		total_monto_ejercido_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_ejercido'))
		total_monto_ejercido = total_monto_ejercido_dict['monto_ejercido__sum']

		total_monto_por_ejercer_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_por_ejercer'))
		total_monto_por_ejercer = total_monto_por_ejercer_dict['monto_por_ejercer__sum']
		
		context = {
		'partida': partida,
		'meses': meses,
		'capitulo': capitulo,
		'programa': programa,
		'total_monto_autorizado': total_monto_autorizado,
		'total_monto_ampliacion': total_monto_ampliacion,
		'total_monto_reduccion': total_monto_reduccion,
		'total_monto_modificado': total_monto_modificado,
		'total_monto_ejercido': total_monto_ejercido,
		'total_monto_por_ejercer': total_monto_por_ejercer,
		}
		return render(request, template_name, context)

class CreateViewPrograma(CreateView):
	model = Programa
	success_url = reverse_lazy('presupuesto:ListViewProgramas')
	fields = ['departamento', 'nombre', 'objetivo', 'actividad', 'meta', 'unidad_de_medida', 
		'fuente_de_financiamiento', 'beneficiarios', 'oficio_de_autorizacion', 'año']

class UpdateViewPrograma(UpdateView):
	model = Programa
	success_url = reverse_lazy('presupuesto:ListViewProgramas')
	fields = ['departamento', 'nombre', 'objetivo', 'actividad', 'meta', 'unidad_de_medida', 
		'fuente_de_financiamiento', 'beneficiarios', 'oficio_de_autorizacion', 'año',]

class DeleteViewPrograma(DeleteView):
	model = Programa
	success_url = reverse_lazy('presupuesto:ListViewProgramas')


class CreateViewCapitulo(View):
	def get(self, request, pk):
		template_name = "presupuesto/createCapitulo.html"
		programa = get_object_or_404(Programa, pk=pk)
		NuevoCapituloForm=CapituloCreateForm()
		context = {
		'programa': programa,
		'NuevoCapituloForm': NuevoCapituloForm,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		template_name = "presupuesto/createCapitulo.html"
		programa = get_object_or_404(Programa, pk=pk)
		NuevoCapituloForm=CapituloCreateForm(request.POST)
		if NuevoCapituloForm.is_valid:
			NuevoCapitulo = NuevoCapituloForm.save(commit=False)
			NuevoCapitulo.programa = programa
			NuevoCapitulo.save()
		return redirect("presupuesto:ListViewCapitulos", pk=programa.pk)

class UpdateViewCapitulo(View):
	def get(self, request, pk):
		template_name = "presupuesto/updateCapitulo.html"
		capitulo = get_object_or_404(Capitulo, pk=pk)
		programa = Programa.objects.get(capitulo=capitulo)
		EdicionCapituloForm=CapituloCreateForm(instance=capitulo)
		context = {
		'programa': programa,
		'EdicionCapituloForm': EdicionCapituloForm,
		}
		return render(request, template_name, context)
	def post(self,request, pk):
		template_name = "presupuesto/updateCapitulo.html"
		capitulo = get_object_or_404(Capitulo, pk=pk)
		programa = Programa.objects.get(capitulo=capitulo)
		EdicionCapituloForm=CapituloCreateForm(instance=capitulo, data=request.POST)
		if EdicionCapituloForm.is_valid:
			EdicionCapituloForm.save()
		return redirect("presupuesto:ListViewCapitulos", pk=programa.pk)

class DeleteViewCapitulo(View):
	def get(self, request, pk):
		template_name = "presupuesto/deleteCapitulo.html"
		capitulo = get_object_or_404(Capitulo, pk=pk)
		programa = Programa.objects.get(capitulo=capitulo)
		context = {
		'capitulo': capitulo,
		'programa': programa,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		template_name = "presupuesto/deleteCapitulo.html"
		capitulo = get_object_or_404(Capitulo, pk=pk)
		programa = Programa.objects.get(capitulo=capitulo)
		if request.method=='POST':
			capitulo.delete()
		return redirect("presupuesto:ListViewCapitulos", pk=programa.pk)

class CreateViewPartida(View):
	def get(self, request, pk):
		template_name = "presupuesto/createPartida.html"
		capitulo = get_object_or_404(Capitulo, pk=pk)
		NuevaPartidaForm=PartidaCreateForm()
		context = {
		'capitulo': capitulo,
		'NuevaPartidaForm': NuevaPartidaForm,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		template_name = "presupuesto/createPartida.html"
		capitulo = get_object_or_404(Capitulo, pk=pk)
		NuevaPartidaForm=PartidaCreateForm(request.POST)
		if NuevaPartidaForm.is_valid:
			NuevaPartida = NuevaPartidaForm.save(commit=False)
			NuevaPartida.capitulo = capitulo
			NuevaPartida.save()
		return redirect("presupuesto:ListViewPartidas", pk=capitulo.pk)

class UpdateViewPartida(View):
	def get(self, request, pk):
		template_name = "presupuesto/updatePartida.html"
		partida = get_object_or_404(Partida, pk=pk)
		capitulo = Capitulo.objects.get(partida=partida)
		EdicionPartidaForm = PartidaCreateForm(instance=partida)
		context = {
			'partida': partida,
			'capitulo': capitulo,
			'EdicionPartidaForm': EdicionPartidaForm,
		}
		return render(request, template_name, context)
	def post(self,request, pk):
		template_name = "presupuesto/updatePartida.html"
		partida = get_object_or_404(Partida, pk=pk)
		capitulo = Capitulo.objects.get(partida=partida)
		EdicionPartidaForm = PartidaCreateForm(instance=partida, data=request.POST)
		if EdicionPartidaForm.is_valid:
			EdicionPartidaForm.save()
		return redirect("presupuesto:ListViewPartidas", pk=capitulo.pk)

class DeleteViewPartida(View):
	def get(self, request, pk):
		template_name = "presupuesto/deletePartida.html"
		partida = get_object_or_404(Partida, pk=pk)
		capitulo = Capitulo.objects.get(partida=partida)
		context = {
		'partida': partida,
		'capitulo': capitulo,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		template_name = "presupuesto/deletePartida.html"
		partida = get_object_or_404(Partida, pk=pk)
		capitulo = Capitulo.objects.get(partida=partida)
		if request.method=='POST':
			partida.delete()
		return redirect("presupuesto:ListViewPartidas", pk=capitulo.pk)

class CreateViewMes(View):
	def get(self, request, pk):
		template_name = "presupuesto/createMes.html"
		partida = get_object_or_404(Partida, pk=pk)
		NuevoMesForm=MesCreateForm()
		context = {
		'partida': partida,
		'NuevoMesForm': NuevoMesForm,
		}
		return render(request, template_name, context)
	def post(self,request, pk):
		template_name = "presupuesto/createMes.html"		
		partida = get_object_or_404(Partida, pk=pk)
		NuevoMesForm = MesCreateForm(request.POST)
		if NuevoMesForm.is_valid:
			NuevoMes = NuevoMesForm.save(commit=False)
			NuevoMes.partida = partida
			NuevoMes.save()
		return redirect("presupuesto:ListViewMeses", pk=partida.pk)

class UpdateViewMes(View):
	def get(self, request, pk):
		template_name = "presupuesto/updateMes.html"
		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		EdicionMesForm = MesEditForm(instance=mes)
		context = {
		'mes': mes,
		'partida': partida,
		'EdicionMesForm': EdicionMesForm,
		}
		return render(request, template_name, context)
	def post(self,request, pk):
		template_name = "presupuesto/updateMes.html"
		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		
		EdicionMesForm = MesEditForm(instance=mes, data=request.POST)

		if EdicionMesForm.is_valid():
			EdicionMesForm.save()
		return redirect("presupuesto:ListViewMeses", pk=partida.pk)

class DeleteViewMes(View):
	def get(self, request, pk):
		template_name = "presupuesto/deleteMes.html"
		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		context = {
		'mes': mes,
		'partida': partida,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		template_name = "presupuesto/deleteMes.html"
		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		if request.method=='POST':
			mes.delete()
		return redirect("presupuesto:ListViewMeses", pk=partida.pk)

class UpdateViewMesAmpliacion(View):
	def get(self, request, pk):
		template_name = "presupuesto/updateMesAmpliacion.html"
		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		NuevaModificacionForm = ModificacionForm()
		context = {
		'mes': mes,
		'partida': partida,
		'NuevaModificacionForm': NuevaModificacionForm
		}
		return render(request, template_name, context)	
	def post(self,request, pk):
		template_name = "presupuesto/updateMesAmpliacion.html"
		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		NuevaModificacionForm = ModificacionForm(request.POST)
		if NuevaModificacionForm.is_valid():
			ampliacion = NuevaModificacionForm.cleaned_data['cantidad']
			mes.monto_ampliacion = ampliacion + mes.monto_ampliacion
			mes.save()
		return redirect("presupuesto:ListViewMeses", pk=partida.pk)

class UpdateViewMesReduccion(View):
	def get(self, request, pk):
		template_name = "presupuesto/updateMesReduccion.html"
		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		NuevaModificacionForm = ModificacionForm()
		context = {
		'mes': mes,
		'partida': partida,
		'NuevaModificacionForm': NuevaModificacionForm
		}
		return render(request, template_name, context)	
	def post(self,request, pk):
		template_name = "presupuesto/updateMesReduccion.html"
		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		NuevaModificacionForm = ModificacionForm(request.POST)
		if NuevaModificacionForm.is_valid():
			reduccion = NuevaModificacionForm.cleaned_data['cantidad']
			mes.monto_reduccion = reduccion + mes.monto_reduccion
			mes.save()
		return redirect("presupuesto:ListViewMeses", pk=partida.pk)

class UpdateViewMesEjercido(View):
	def get(self, request, pk):
		template_name = "presupuesto/updateMesEjercido.html"
		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		NuevaModificacionForm = ModificacionForm()
		context = {
		'mes': mes,
		'partida': partida,
		'NuevaModificacionForm': NuevaModificacionForm
		}
		return render(request, template_name, context)	
	def post(self,request, pk):
		template_name = "presupuesto/updateMesEjercido.html"
		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		NuevaModificacionForm = ModificacionForm(request.POST)
		if NuevaModificacionForm.is_valid():
			ejercido = NuevaModificacionForm.cleaned_data['cantidad']
			if ejercido > mes.monto_por_ejercer:
				messages.error(request, "Error, el monto a ejercer es mayor que la cantidad dispoble por ejercer")
				context = {
					'mes': mes,
					'partida': partida,
					'NuevaModificacionForm': NuevaModificacionForm
				}
				return render(request,template_name,context)
			else:
				mes.monto_ejercido = ejercido + mes.monto_ejercido
				mes.save()
		return redirect("presupuesto:ListViewMeses", pk=partida.pk)