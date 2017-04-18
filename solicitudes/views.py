from django.shortcuts import render, redirect
from django.views.generic import View 
from .models import *
from .forms import *
from accounts.models import Perfil
import datetime
from presupuesto.models import *

class ListViewSolicitudesPropias(View):
	#@method_decorator(login_required)
	def get(self, request):

		template_name = "solicitudes/listSolitudesPropias.html"
		hoy = datetime.datetime.now()

		solicitudes = SolicitudRecursoFinanciero.objects.filter(creacion__year=hoy.year, creacion__month=hoy.month, solicitante=request.user)

		context = {
			'solicitudes': solicitudes,
		}
		return render(request,template_name,context)

class CreateViewSolicitudEmpleado(View):
	def get(self, request):
		template_name = "solicitudes/createSolicitudEmpleado.html"

		hoy = datetime.datetime.now()

		user = User.objects.get(pk=request.user.pk)
		departamento = Departamento.objects.get(user=user)
		folio = str(departamento.codigo) + "-" + str(SolicitudRecursoFinanciero.objects.filter(folio__contains=departamento.codigo, creacion__year=hoy.year).count() + 1) + "-" + str(hoy.year)

		programas = Programa.objects.filter(año=hoy.year, departamento=departamento)
		print(SolicitudRecursoFinanciero.objects.filter(folio__contains=departamento.codigo, creacion__year=hoy.year))
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

		hoy = datetime.datetime.now()

		user = User.objects.get(pk=request.user.pk)
		departamento = Departamento.objects.get(user=user)
		folio = str(departamento.codigo) + "-" + str(SolicitudRecursoFinanciero.objects.filter(folio__contains=departamento.codigo, creacion__year=hoy.year).count() + 1) + "-" + str(hoy.year)
		NuevoSolicitudRecursoFinancieroForm = SolicitudRecursoFinancieroCreateForm(data=request.POST)
		
		empleado = User.objects.get(pk=request.POST.get("a_nombre_de"))
		perfilEmpleado = Perfil.objects.get(user=empleado)

		if NuevoSolicitudRecursoFinancieroForm.is_valid(): 
			NuevoSolicitudRecursoFinanciero = NuevoSolicitudRecursoFinancieroForm.save(commit=False)
			NuevoSolicitudRecursoFinanciero.folio = folio
			NuevoSolicitudRecursoFinanciero.clabe =  perfilEmpleado.CLABE
			NuevoSolicitudRecursoFinanciero.solicitante = user
			NuevoSolicitudRecursoFinanciero.save()

		return redirect("solicitudes:ListViewSolicitudesPropias")

class CreateViewSolicitudProveedor(View):
	def get(self, request):
		template_name = "solicitudes/createSolicitudProveedor.html"

		hoy = datetime.datetime.now()

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

		hoy = datetime.datetime.now()

		user = User.objects.get(pk=request.user.pk)
		departamento = Departamento.objects.get(user=user)
		folio = str(departamento.codigo) + "-" + str(SolicitudRecursoFinanciero.objects.filter(folio__contains=departamento.codigo, creacion__year=hoy.year).count() + 1) + "-" + str(hoy.year)
		NuevoSolicitudRecursoFinancieroForm = SolicitudRecursoFinancieroCreateForm2(request.POST, request.FILES)
		
		proveedor = User.objects.get(pk=request.POST.get("a_nombre_de"))
		perfilProveedor = Perfil.objects.get(user=proveedor)

		if NuevoSolicitudRecursoFinancieroForm.is_valid(): 
			NuevoSolicitudRecursoFinanciero = NuevoSolicitudRecursoFinancieroForm.save(commit=False)
			NuevoSolicitudRecursoFinanciero.folio = folio
			NuevoSolicitudRecursoFinanciero.clabe =  perfilProveedor.CLABE
			NuevoSolicitudRecursoFinanciero.solicitante = user
			NuevoSolicitudRecursoFinanciero.save()

		return redirect("solicitudes:ListViewSolicitudesPropias")

class DetailViewSolicitudPropia(View):
	def get(self, request, pk):
		template_name = "solicitudes/detailSolicitudPropia.html"
		solicitud = get_object_or_404(SolicitudRecursoFinanciero, pk=pk)
		context = {
			'solicitud': solicitud
		}
		return render(request, template_name, context)

class ListViewSolicitudesPendientes(View):
	#@method_decorator(login_required)
	def get(self, request):

		template_name = "solicitudes/listSolitudesPendientes.html"
		hoy = datetime.datetime.now()

		solicitudes = SolicitudRecursoFinanciero.objects.filter(pagado=False)

		context = {
			'solicitudes': solicitudes,
		}
		return render(request,template_name,context)

class DetailViewSolicitudPendiente(View):
	def get(self, request, pk):
		template_name = "solicitudes/detailSolicitudPendiente.html"
		solicitud = get_object_or_404(SolicitudRecursoFinanciero, pk=pk)
		EdicionSolicitudForm=SolicitudRecursoFinancieroEditForm(instance=solicitud)
		context = {
			'solicitud': solicitud,
			'EdicionSolicitudForm': EdicionSolicitudForm,
		}
		return render(request, template_name, context)
	def post (self, request, pk):
		template_name = "solicitudes/detailSolicitudPendiente.html"
		solicitud = get_object_or_404(SolicitudRecursoFinanciero, pk=pk)
		EdicionSolicitudForm=SolicitudRecursoFinancieroEditForm(instance=solicitud, data=request.POST)

		if EdicionSolicitudForm.is_valid():
			EdicionSolicitudForm.save()

		return redirect("solicitudes:DetailViewSolicitudPendiente", pk=solicitud.pk)