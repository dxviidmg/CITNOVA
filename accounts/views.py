from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import *
from django.db.models import Count
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#Lista de empleados
class ListViewEmpleados(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/ListViewEmpleados.html"

		empleados = User.objects.filter(departamento=request.user.departamento, is_active=True).order_by('username')

		context = {
			'empleados': empleados,
		}
		return render(request,template_name,context)

#Lista de proveedores
class ListViewProveedores(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/ListViewProveedores.html"

		proveedores = User.objects.filter(is_staff=False, is_active=True, username__startswith='PROV').order_by('username')

		context = {
			'proveedores': proveedores
		}
		return render(request,template_name,context)

#Creación de un empleado
class CreateViewEmpleado(View):
	@method_decorator(login_required)
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

#Creación de un Proveedor
class CreateViewProveedor(View):
	@method_decorator(login_required)
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

#Edición de un empleado
class UpdateViewEmpleado(View):
	@method_decorator(login_required)
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

			messages.success(request, "Se han gaurdado los cambios correctamente")
		return redirect("accounts:UpdateViewEmpleado", pk=user.pk)

#Edición de un proveedor
class UpdateViewProveedor(View):
	@method_decorator(login_required)
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

			messages.success(request, "Se han gaurdado los cambios correctamente")

		return redirect("accounts:UpdateViewProveedor", pk=user.pk)

#Desactivación de un empleado o proveedor
class DesactivateViewUser(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "accounts/desactivateUser.html"
		user = get_object_or_404(User, pk=pk)
		perfil = Perfil.objects.get(user=user)
		expediente = Expediente.objects.filter(perfil=perfil)

		DesactivaUserForm = UserDesactivateForm(instance=user)
	
		context = {
			'user': user,
			'perfil': perfil,
			'DesactivaUserForm': DesactivaUserForm,
		}
		return render(request, template_name, context)
	def post(self,request, pk):
		template_name = "accounts/desactivateUser.html"
		user = get_object_or_404(User, pk=pk)
		perfil = Perfil.objects.get(user=user)
		expediente = Expediente.objects.filter(perfil=perfil)

		DesactivaUserForm = UserDesactivateForm(instance=user, data=request.POST)
	
		if DesactivaUserForm.is_valid:
			DesactivaUserForm.save()

		if request.user.username == "administrador":
			return redirect("accounts:ListViewDirectores")
		else:
			if expediente.exists():
				return redirect("accounts:ListViewProveedores")
			else:
				return redirect("accounts:ListViewEmpleados")

#Lista de bancos
class ListViewBancos(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/listBancos.html"
		bancos = Banco.objects.all()
		context = {
			'bancos': bancos
		}
		return render(request,template_name, context)

#Creación de bancos
class CreateViewBanco(CreateView):
	model = Banco
	success_url = reverse_lazy('accounts:ListViewBancos')
	fields = ['nombre',]

#Edición de bancos
class UpdateViewBanco(UpdateView):
	model = Banco
	success_url = reverse_lazy('accounts:ListViewBancos')
	fields = ['nombre',]

#Borrado de Bancos
class DeleteViewBanco(DeleteView):
	model = Banco
	success_url = reverse_lazy('accounts:ListViewBancos')

#Perfil de usuario autenticado
class profile(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/profile.html"
		perfil = Perfil.objects.get(user=request.user)
		
		context = {
			'perfil': perfil
		}		
		return render(request,template_name, context)

#Lista de bancos
class ListViewDepartamentos(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/listDepartamentos.html"
		departamentos = Departamento.objects.all()
		context = {
			'departamentos': departamentos
		}
		return render(request,template_name, context)

#Creación de Departamentos
class CreateViewDepartamento(CreateView):
	model = Departamento
	success_url = reverse_lazy('accounts:ListViewDepartamentos')
	fields = ['nombre','codigo',]

#Edicion de Departamentos
class UpdateViewDepartamento(UpdateView):
	model = Departamento
	success_url = reverse_lazy('accounts:ListViewDepartamentos')
	fields = ['nombre','codigo',]

#Borrado de Departamentos
class DeleteViewDepartamento(DeleteView):
	model = Departamento
	success_url = reverse_lazy('accounts:ListViewDepartamentos')

#Lista de directores
class ListViewDirectores(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/ListViewDirectores.html"

		users = User.objects.filter(is_active=True).order_by('username')

		directores = []
		for user in users:
			try:
				perfil = Perfil.objects.get(user=user)
				if perfil.puesto == "Director":		
					directores.append({'user': user, 'perfil':Perfil.objects.filter(user=user)})
			except Exception as e:
				directores = []
		print()
		context = {
			'directores': directores
		}
		return render(request,template_name,context)

#Creación de un Director
class CreateViewDirector(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/createDirector.html"
		
		UserDirectorForm = UserDirectorCreateForm()
		PerfilDirectorForm = PerfilDirectorCreateForm()
		
		context = {
			'UserDirectorForm': UserDirectorForm,
			'PerfilDirectorForm': PerfilDirectorForm,
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name = "accounts/createDirector.html"

		NuevoUserForm = UserDirectorCreateForm(request.POST)
		NuevoPerfilForm = PerfilDirectorCreateForm(request.POST)

		if NuevoUserForm.is_valid(): 
			NuevoUser = NuevoUserForm.save(commit=False)
			NuevoUser.set_password(NuevoUserForm.cleaned_data['password'])
			NuevoUser.save()

		if NuevoPerfilForm.is_valid():
			NuevoPerfil = NuevoPerfilForm.save(commit=False)
			NuevoPerfil.user = NuevoUser
			NuevoPerfil.puesto = "Director"
			NuevoPerfil.save()

		else:			
			context = {
				'UserDirectorForm': UserDirectorForm,
				'PerfilDirectorForm': PerfilDirectorForm,
				
			}
			return render(request,template_name,context)

		return redirect("accounts:ListViewDirectores")

#Edición de un Director
class UpdateViewDirector(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "accounts/updateDirector.html"
		user = get_object_or_404(User, pk=pk)
		perfil = Perfil.objects.get(user=user)

		EdicionDirectorForm=UserDirectorEditForm(instance=user)
		EdicionPerfilForm=PerfilDirectorCreateForm(instance=perfil)
	
		context = {
			'EdicionDirectorForm': EdicionDirectorForm,
			'EdicionPerfilForm': EdicionPerfilForm,
		}
		return render(request, template_name, context)
	def post(self,request, pk):
		template_name = "accounts/updateDirector.html"
		user = get_object_or_404(User, pk=pk)
		perfil = Perfil.objects.get(user=user)

		EdicionDirectorForm=UserDirectorEditForm(instance=user, data=request.POST)
		EdicionPerfilForm=PerfilDirectorCreateForm(instance=perfil, data=request.POST)

		if EdicionDirectorForm.is_valid:
			EdicionDirectorForm.save()

		if EdicionPerfilForm.is_valid:
			EdicionPerfilForm.save()

			messages.success(request, "Se han gaurdado los cambios correctamente")
		return redirect("accounts:UpdateViewDirector", pk=user.pk)