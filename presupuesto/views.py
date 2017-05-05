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
from accounts.models import Perfil
from solicitudes.forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#Lista de programas
class ListViewProgramas(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "presupuesto/listProgramas.html"
		hoy = datetime.datetime.now()
		user = request.user
		
		if user.departamento is None:
			programas = Programa.objects.filter(año=hoy.year).order_by('nombre')
		else:
			programas = Programa.objects.filter(año=hoy.year, departamento=user.departamento).order_by('nombre')
	
		context = {
			'programas': programas,
		}
		return render(request, template_name, context)

#Lista de capitulos
class ListViewCapitulos(View):
	@method_decorator(login_required)
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

#Lista de partidas
class ListViewPartidas(View):
	@method_decorator(login_required)
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

#Lista de Meses
class ListViewMeses(View):
	@method_decorator(login_required)
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

#Creación de un programa
class CreateViewPrograma(CreateView):
	model = Programa
	success_url = reverse_lazy('presupuesto:ListViewProgramas')
	fields = ['departamento', 'nombre', 'objetivo', 'actividad', 'meta', 'unidad_de_medida', 
		'fuente_de_financiamiento', 'beneficiarios', 'oficio_de_autorizacion', 'año']

#Edición de un Programa
class UpdateViewPrograma(UpdateView):
	model = Programa
	success_url = reverse_lazy('presupuesto:ListViewProgramas')
	fields = ['departamento', 'nombre', 'objetivo', 'actividad', 'meta', 'unidad_de_medida', 
		'fuente_de_financiamiento', 'beneficiarios', 'oficio_de_autorizacion', 'año',]

#Borrado de un Programa
class DeleteViewPrograma(DeleteView):
	model = Programa
	success_url = reverse_lazy('presupuesto:ListViewProgramas')

#Creación de un Capitulo
class CreateViewCapitulo(View):
	@method_decorator(login_required)
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

#Edición de un Capitulo
class UpdateViewCapitulo(View):
	@method_decorator(login_required)
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

#Borrado de un Capitulo
class DeleteViewCapitulo(View):
	@method_decorator(login_required)
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

#Creación de una Partida
class CreateViewPartida(View):
	@method_decorator(login_required)
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

#Edicióm de una Partida
class UpdateViewPartida(View):
	@method_decorator(login_required)
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

#Borrado de una Partida
class DeleteViewPartida(View):
	@method_decorator(login_required)
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

#Creación de un Mes
class CreateViewMes(View):
	@method_decorator(login_required)
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

#Edición de un Mes
class UpdateViewMes(View):
	@method_decorator(login_required)
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

#Borrado de un Mes
class DeleteViewMes(View):
	@method_decorator(login_required)
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

#Realización de una Ampliación
class UpdateViewMesAmpliacion(View):
	@method_decorator(login_required)
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

#Realización de una Reducción
class UpdateViewMesReduccion(View):
	@method_decorator(login_required)
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

#Realización de una Ejerción (Solicitud de RF para empleados)
class UpdateViewMesEjercido(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		hoy = datetime.datetime.now()

		template_name = "presupuesto/updateMesEjercido.html"
		user = request.user
		departamento = Departamento.objects.get(user=user)
		folio = str(departamento.codigo) + "-" + str(SolicitudRecursoFinanciero.objects.filter(folio__contains=departamento.codigo, creacion__year=hoy.year).count() + 1) + "-" + str(hoy.year)

		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		capitulo = Capitulo.objects.get(partida=partida)
		programa = Programa.objects.get(capitulo=capitulo)

		NuevaModificacionForm = ModificacionForm()
		NuevaSolicitudForm = SolicitudRecursoFinancieroCreateForm(departamento=departamento)
		context = {
			'folio': folio,
			'mes': mes,
			'partida': partida,
			'NuevaModificacionForm': NuevaModificacionForm,
			'NuevaSolicitudForm': NuevaSolicitudForm,
		}
		return render(request, template_name, context)	
	def post(self,request, pk):
		hoy = datetime.datetime.now()

		template_name = "presupuesto/updateMesEjercido.html"
		user = request.user
		departamento = Departamento.objects.get(user=user)
		folio = str(departamento.codigo) + "-" + str(SolicitudRecursoFinanciero.objects.filter(folio__contains=departamento.codigo, creacion__year=hoy.year).count() + 1) + "-" + str(hoy.year)

		empleado = User.objects.get(pk=request.POST.get("a_nombre_de"))
		perfilEmpleado = Perfil.objects.get(user=empleado)

		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		capitulo = Capitulo.objects.get(partida=partida)
		programa = Programa.objects.get(capitulo=capitulo)

		NuevaModificacionForm = ModificacionForm(request.POST)
		NuevaSolicitudForm = SolicitudRecursoFinancieroCreateForm(departamento=departamento, data=request.POST, files=request.FILES)

		if NuevaSolicitudForm.is_valid():
			ejercido = NuevaSolicitudForm.cleaned_data['importe_numero']
			if ejercido > mes.monto_por_ejercer:
				messages.error(request, "Error, el monto a ejercer es mayor que la cantidad dispoble por ejercer")
				context = {
					'folio': folio,
					'mes': mes,
					'partida': partida,
					'NuevaModificacionForm': NuevaModificacionForm,
					'NuevaSolicitudForm': NuevaSolicitudForm,				}
				return render(request,template_name,context)
			else:
				mes.monto_ejercido = ejercido + mes.monto_ejercido
				mes.save()

				NuevaSolicitud = NuevaSolicitudForm.save(commit=False)
				NuevaSolicitud.folio = folio
				NuevaSolicitud.clabe =  perfilEmpleado.CLABE
				NuevaSolicitud.solicitante = user
				NuevaSolicitud.mes = mes
				NuevaSolicitud.cuenta_bancaria_del_programa = programa.cuenta_bancaria
				NuevaSolicitud.save()
		return redirect("solicitudes:ListViewSolicitudesPorMes", pk=mes.pk)

#Realización de una Ejerción (Solicitud de RF para proveedores)
class UpdateViewMesEjercido2(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		hoy = datetime.datetime.now()

		template_name = "presupuesto/updateMesEjercido2.html"
		user = request.user
		departamento = Departamento.objects.get(user=user)
		folio = str(departamento.codigo) + "-" + str(SolicitudRecursoFinanciero.objects.filter(folio__contains=departamento.codigo, creacion__year=hoy.year).count() + 1) + "-" + str(hoy.year)

		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		capitulo = Capitulo.objects.get(partida=partida)
		programa = Programa.objects.get(capitulo=capitulo)

		NuevaModificacionForm = ModificacionForm()
		NuevaSolicitudForm = SolicitudRecursoFinancieroCreateForm2()
		context = {
			'folio': folio,
			'mes': mes,
			'partida': partida,
			'NuevaModificacionForm': NuevaModificacionForm,
			'NuevaSolicitudForm': NuevaSolicitudForm,
		}
		return render(request, template_name, context)	
	def post(self,request, pk):
		hoy = datetime.datetime.now()

		template_name = "presupuesto/updateMesEjercido.html"
		user = request.user
		departamento = Departamento.objects.get(user=user)
		folio = str(departamento.codigo) + "-" + str(SolicitudRecursoFinanciero.objects.filter(folio__contains=departamento.codigo, creacion__year=hoy.year).count() + 1) + "-" + str(hoy.year)

		empleado = User.objects.get(pk=request.POST.get("a_nombre_de"))
		perfilEmpleado = Perfil.objects.get(user=empleado)

		mes = get_object_or_404(Mes, pk=pk)
		partida = Partida.objects.get(mes=mes)
		capitulo = Capitulo.objects.get(partida=partida)
		programa = Programa.objects.get(capitulo=capitulo)

		NuevaModificacionForm = ModificacionForm(request.POST)
		NuevaSolicitudForm = SolicitudRecursoFinancieroCreateForm2(data=request.POST, files=request.FILES)

		if NuevaSolicitudForm.is_valid():
			ejercido = NuevaSolicitudForm.cleaned_data['importe_numero']
			if ejercido > mes.monto_por_ejercer:
				messages.error(request, "Error, el monto a ejercer es mayor que la cantidad dispoble por ejercer")
				context = {
					'folio': folio,
					'mes': mes,
					'partida': partida,
					'NuevaModificacionForm': NuevaModificacionForm,
					'NuevaSolicitudForm': NuevaSolicitudForm,				}
				return render(request,template_name,context)
			else:
				mes.monto_ejercido = ejercido + mes.monto_ejercido
				mes.save()

				NuevaSolicitud = NuevaSolicitudForm.save(commit=False)
				NuevaSolicitud.folio = folio
				NuevaSolicitud.clabe =  perfilEmpleado.CLABE
				NuevaSolicitud.solicitante = user
				NuevaSolicitud.mes = mes
				NuevaSolicitud.cuenta_bancaria_del_programa = programa.cuenta_bancaria
				NuevaSolicitud.save()
		return redirect("solicitudes:ListViewSolicitudesPorMes", pk=mes.pk)	