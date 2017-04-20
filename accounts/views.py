from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import *
from django.db.models import Count
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class ListViewEmpleados(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/ListViewEmpleados.html"

		empleados = User.objects.filter(departamento=request.user.departamento).order_by('username')

		context = {
			'empleados': empleados,
		}
		return render(request,template_name,context)

class ListViewProveedores(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/ListViewProveedores.html"

		proveedores = User.objects.filter(is_staff=False, is_active=True, username__startswith='PROV').order_by('username')

		context = {
			'proveedores': proveedores
		}
		return render(request,template_name,context)

class CreateViewEmpleado(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/createEmpleado.html"
		
		UserEmpleadoForm = UserEmpleadoCreateForm()
		PerfilEmpleadoForm = PerfilEmpleadoCreateForm()
		
		context = {
			'UserEmpleadoForm': UserEmpleadoForm,
			'PerfilEmpleadoForm': PerfilEmpleadoForm,
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name = "accounts/createEmpleado.html"

		users = User.objects.filter(is_staff=False).count()
		userActual = users + 1

		NuevoUserForm = UserEmpleadoCreateForm(request.POST)
		NuevoPerfilForm = PerfilEmpleadoCreateForm(request.POST)
		
		if NuevoUserForm.is_valid(): 
			NuevoUser = NuevoUserForm.save(commit=False)
			NuevoUser.username = 'EMPL' + str(NuevoUser.first_name[0].upper()) + str(NuevoUser.last_name[0].upper()) + str(userActual)
			NuevoUser.save()

		if NuevoPerfilForm.is_valid():
			NuevoPerfil = NuevoPerfilForm.save(commit=False)
			NuevoPerfil.user = NuevoUser
			NuevoPerfil.save()
		return redirect("accounts:ListViewEmpleados")

class CreateViewProveedor(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/createProveedor.html"
		
		UserProveedorForm = UserProveedorCreateForm()
		PerfilProveedorForm = PerfilProveedorCreateForm()
		ExpedienteProveedorForm = ExpedienteProveedorCreateForm()
		
		context = {
			'UserProveedorForm': UserProveedorForm,
			'PerfilProveedorForm': PerfilProveedorForm,
			'ExpedienteProveedorForm': ExpedienteProveedorForm,
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name = "accounts/createProveedor.html"

		users = User.objects.filter(is_staff=False).count()
		userActual = users + 1

		NuevoUserForm = UserProveedorCreateForm(request.POST)		
		NuevoPerfilForm = PerfilProveedorCreateForm(request.POST)
		NuevoExpedienteForm = ExpedienteProveedorCreateForm(request.POST, request.FILES)

		if NuevoUserForm.is_valid(): 
			NuevoUser = NuevoUserForm.save(commit=False)
			NuevoUser.username = 'PROV' + str(NuevoUser.first_name[0].upper()) + str(NuevoUser.last_name[0].upper()) + str(userActual)
			NuevoUser.save()


		if NuevoPerfilForm.is_valid():
			NuevoPerfil = NuevoPerfilForm.save(commit=False)
			NuevoPerfil.user = NuevoUser
			NuevoPerfil.save()

		if NuevoExpedienteForm.is_valid():
			NuevoExpediente = NuevoExpedienteForm.save(commit=False)
			NuevoExpediente.perfil = NuevoPerfil
			NuevoExpediente.save()
			
		return redirect("accounts:ListViewProveedores")

class profile(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/profile.html"
		return render(request,template_name)

class UpdateViewEmpleado(View):
	def get(self, request, pk):
		template_name = "accounts/updateEmpleado.html"
		user = get_object_or_404(User, pk=pk)
		perfil = Perfil.objects.get(user=user)

		EdicionEmpleadoForm=UserEmpleadoCreateForm(instance=user)
		EdicionPerfilForm=PerfilEmpleadoCreateForm(instance=perfil)
	
		context = {
			'EdicionEmpleadoForm': EdicionEmpleadoForm,
			'EdicionPerfilForm': EdicionPerfilForm,
		}
		return render(request, template_name, context)
	def post(self,request, pk):
		template_name = "accounts/updateEmpleado.html"
		user = get_object_or_404(User, pk=pk)
		perfil = Perfil.objects.get(user=user)

		EdicionEmpleadoForm=UserEmpleadoCreateForm(instance=user, data=request.POST)
		EdicionPerfilForm=PerfilEmpleadoCreateForm(instance=perfil, data=request.POST)

		if EdicionEmpleadoForm.is_valid:
			EdicionEmpleadoForm.save()

		if EdicionPerfilForm.is_valid:
			EdicionPerfilForm.save()
		return redirect("accounts:UpdateViewEmpleado", pk=user.pk)

class UpdateViewProveedor(View):
	def get(self, request, pk):
		template_name = "accounts/updateProveedor.html"
		user = get_object_or_404(User, pk=pk)
		perfil = Perfil.objects.get(user=user)
		expediente = Expediente.objects.get(perfil=perfil)

		EdicionProveedorForm=UserProveedorCreateForm(instance=user)
		EdicionPerfilForm=PerfilProveedorCreateForm(instance=perfil)
		EdicionExpedienteForm=ExpedienteProveedorCreateForm(instance=expediente)
		context = {
			'expediente': expediente,
			'EdicionProveedorForm': EdicionProveedorForm,
			'EdicionPerfilForm': EdicionPerfilForm,
			'EdicionExpedienteForm': EdicionExpedienteForm
		}
		return render(request, template_name, context)
	def post(self,request, pk):
		template_name = "accounts/updateProveedor.html"
		user = get_object_or_404(User, pk=pk)
		perfil = Perfil.objects.get(user=user)
		expediente = Expediente.objects.get(perfil=perfil)
		
		EdicionProveedorForm=UserProveedorCreateForm(instance=user, data=request.POST)
		EdicionPerfilForm=PerfilProveedorCreateForm(instance=perfil, data=request.POST)
		EdicionExpedienteForm=ExpedienteProveedorCreateForm(instance=expediente, data=request.POST, files=request.FILES)
		
		if EdicionProveedorForm.is_valid:
			EdicionProveedorForm.save()

		if EdicionPerfilForm.is_valid:
			EdicionPerfilForm.save()

		if EdicionExpedienteForm.is_valid():
			EdicionExpedienteForm.save()

		return redirect("accounts:UpdateViewProveedor", pk=user.pk)

class ListViewBancos(View):
	def get(self, request):
		template_name = "accounts/listBancos.html"
		bancos = Banco.objects.all()
		context = {
			'bancos': bancos
		}
		return render(request,template_name, context)

class CreateViewBanco(CreateView):
	model = Banco
	success_url = reverse_lazy('accounts:ListViewBancos')
	fields = ['nombre',]

class UpdateViewBanco(UpdateView):
	model = Banco
	success_url = reverse_lazy('accounts:ListViewBancos')
	fields = ['nombre',]

class DeleteViewBanco(DeleteView):
	model = Banco
	success_url = reverse_lazy('accounts:ListViewBancos')

class profile(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/profile.html"
		return render(request,template_name)