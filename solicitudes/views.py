from django.shortcuts import render, redirect
from django.views.generic import View 
from .models import *
from .forms import *
from accounts.models import Perfil
import datetime
from presupuesto.models import *
from django.contrib import messages
from datetime import timedelta
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Count

hoy = datetime.datetime.now()
#Lista de solicitudes propias
class ListViewSolicitudesPorMes(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "solicitudes/listSolitudesPorMes.html"
		mes = get_object_or_404(Mes, pk=pk)
		solicitudes = SolicitudRecursoFinanciero.objects.filter(mes=mes)

		context = {
			'solicitudes': solicitudes,
		}
		return render(request,template_name,context)

#Lista de solicitudes creadas por un usuario logeado
class ListViewSolicitudesPropias(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "solicitudes/listSolitudesPropias.html"
		solicitudes = SolicitudRecursoFinanciero.objects.filter(creacion__year=hoy.year, creacion__month=hoy.month, solicitante=request.user)

		context = {
			'solicitudes': solicitudes,
		}
		return render(request,template_name,context)

#Creación de Solicitud para un empleado
class CreateViewSolicitudEmpleado(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "solicitudes/createSolicitudEmpleado.html"
		user = User.objects.get(pk=request.user.pk)
		departamento = Departamento.objects.get(user=user)
		folio = str(departamento.codigo) + "-" + str(SolicitudRecursoFinanciero.objects.filter(folio__contains=departamento.codigo, creacion__year=hoy.year).count() + 1) + "-" + str(hoy.year)

		programas = Programa.objects.filter(año=hoy.year, departamento=departamento)
		SolicitudRecursoFinancieroForm = SolicitudRecursoFinancieroCreateForm(departamento=departamento, )
		context = {
			'departamento': departamento,
			'folio': folio,
			'SolicitudRecursoFinancieroForm': SolicitudRecursoFinancieroForm,
			'programas': programas,
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name = "solicitudes/createSolicitudEmpleado.html"
		user = User.objects.get(pk=request.user.pk)
		departamento = Departamento.objects.get(user=user)
		folio = str(departamento.codigo) + "-" + str(SolicitudRecursoFinanciero.objects.filter(folio__contains=departamento.codigo, creacion__year=hoy.year).count() + 1) + "-" + str(hoy.year)
		NuevoSolicitudRecursoFinancieroForm = SolicitudRecursoFinancieroCreateForm(data=request.POST, files=request.FILES)
		
		empleado = User.objects.get(pk=request.POST.get("a_nombre_de"))
		perfilEmpleado = Perfil.objects.get(user=empleado)

		if NuevoSolicitudRecursoFinancieroForm.is_valid(): 
			NuevoSolicitudRecursoFinanciero = NuevoSolicitudRecursoFinancieroForm.save(commit=False)
			NuevoSolicitudRecursoFinanciero.folio = folio
			NuevoSolicitudRecursoFinanciero.clabe =  perfilEmpleado.CLABE
			NuevoSolicitudRecursoFinanciero.solicitante = user
			NuevoSolicitudRecursoFinanciero.save()

		return redirect("solicitudes:ListViewSolicitudesPropias")

#Creación de Solicitud para un proveedor
class CreateViewSolicitudProveedor(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "solicitudes/createSolicitudProveedor.html"
		user = User.objects.get(pk=request.user.pk)
		departamento = Departamento.objects.get(user=user)
		folio = str(departamento.codigo) + "-" + str(SolicitudRecursoFinanciero.objects.filter(folio__contains=departamento.codigo, creacion__year=hoy.year).count() + 1) + "-" + str(hoy.year)
		SolicitudRecursoFinancieroForm = SolicitudRecursoFinancieroCreateForm2()

		context = {
			'departamento': departamento,
			'folio': folio,
			'SolicitudRecursoFinancieroForm': SolicitudRecursoFinancieroForm,
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name = "solicitudes/createSolicitudProveedor.html"
		user = User.objects.get(pk=request.user.pk)
		departamento = Departamento.objects.get(user=user)
		folio = str(departamento.codigo) + "-" + str(SolicitudRecursoFinanciero.objects.filter(folio__contains=departamento.codigo, creacion__year=hoy.year).count() + 1) + "-" + str(hoy.year)
		NuevoSolicitudRecursoFinancieroForm = SolicitudRecursoFinancieroCreateForm2(data=request.POST, files=request.FILES)
		
		proveedor = User.objects.get(pk=request.POST.get("a_nombre_de"))
		perfilProveedor = Perfil.objects.get(user=proveedor)

		if NuevoSolicitudRecursoFinancieroForm.is_valid(): 
			NuevoSolicitudRecursoFinanciero = NuevoSolicitudRecursoFinancieroForm.save(commit=False)
			NuevoSolicitudRecursoFinanciero.folio = folio
			NuevoSolicitudRecursoFinanciero.clabe =  perfilProveedor.CLABE
			NuevoSolicitudRecursoFinanciero.solicitante = user
			NuevoSolicitudRecursoFinanciero.save()

		return redirect("solicitudes:ListViewSolicitudesPropias")

#Detalle de una Solicitud propia
class DetailViewSolicitudPropia(View):
	def get(self, request, pk):
		template_name = "solicitudes/detailSolicitudPropia.html"
		solicitud = get_object_or_404(SolicitudRecursoFinanciero, pk=pk)
		mes = Mes.objects.get(pk=solicitud.mes.pk)
		partida = Partida.objects.get(mes=mes)
		capitulo = Capitulo.objects.get(partida=partida)
		programa = Programa.objects.get(capitulo=capitulo)
		context = {
			'solicitud': solicitud,
			'mes': mes,
			'partida': partida,
			'capitulo': capitulo,
			'programa': programa,
		}
		return render(request, template_name, context)

#Lista de Solicitudes por pagar
class ListViewSolicitudesPendientes(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "solicitudes/listSolitudesPendientes.html"
		solicitudes = SolicitudRecursoFinanciero.objects.filter(pagado=False)		
		context = {
			'solicitudes': solicitudes,
		}
		return render(request,template_name,context)

#Detalle de una Solicitud por pagar
class DetailViewSolicitudPendiente(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "solicitudes/detailSolicitudPendiente.html"
		solicitud = get_object_or_404(SolicitudRecursoFinanciero, pk=pk)
		EdicionSolicitudForm=SolicitudRecursoFinancieroEditForm(instance=solicitud)
		mes = Mes.objects.get(pk=solicitud.mes.pk)
		partida = Partida.objects.get(mes=mes)
		capitulo = Capitulo.objects.get(partida=partida)
		programa = Programa.objects.get(capitulo=capitulo)
		context = {
			'solicitud': solicitud,
			'EdicionSolicitudForm': EdicionSolicitudForm,
			'mes': mes,
			'partida': partida,
			'capitulo': capitulo,
			'programa': programa,
		}
		return render(request, template_name, context)
	def post (self, request, pk):
		template_name = "solicitudes/detailSolicitudPendiente.html"
		solicitud = get_object_or_404(SolicitudRecursoFinanciero, pk=pk)
		EdicionSolicitudForm=SolicitudRecursoFinancieroEditForm(instance=solicitud, data=request.POST)

		if EdicionSolicitudForm.is_valid():
			EdicionSolicitudForm.save()
			messages.success(request, "Se cambió el estatus correctamente")			

		return redirect("solicitudes:DetailViewSolicitudPendiente", pk=solicitud.pk)

#Lista de solicitudes pagadas en la ultima semana
class ListViewSolicitudesPagadas(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "solicitudes/listSolitudesPagadas.html"
		semana_pasada = hoy - timedelta(days=7)
		solicitudes = SolicitudRecursoFinanciero.objects.filter(fecha_pagado__isnull=False, fecha_pagado__range=[semana_pasada, hoy])
		context = {
			'solicitudes': solicitudes,
		}
		return render(request,template_name,context)

class SearchSolicitudes(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "solicitudes/searchSolitudes.html"
		query = request.GET.get("query")

		if query:
			solicitudes = SolicitudRecursoFinanciero.objects.filter(
				(
					Q(folio__contains=query) | 
					Q(concepto__contains=query) |
					Q(importe_numero__contains=query)
				), 
				creacion__year=hoy.year
			).order_by("-creacion")

			if not solicitudes.exists():
				
				users = User.objects.filter(
					(
						Q(first_name__contains=query) | 
						Q(last_name__contains=query)
					)
				)
				
				solicitudes = SolicitudRecursoFinanciero.objects.filter(
						a_nombre_de=users, 
						creacion__year=hoy.year
					).order_by("-creacion")
	
		else:
			solicitudes = []
	
		context = {
			'solicitudes': solicitudes,
		}
		return render(request,template_name, context)