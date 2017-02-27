from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import *
from django.db.models import Count

class ListViewTodos(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/ListViewTodos.html"

		todos = User.objects.filter(is_staff=False).order_by('username')
		empleados = User.objects.filter(is_staff=False, departamento=request.user.departamento).order_by('username')
		proveedores = User.objects.filter(is_staff=False, departamento__isnull=True).order_by('username')
		context = {
			'todos': todos,
			'empleados': empleados,
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
		return redirect("accounts:ListViewTodos")

class CreateViewProveedor(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/createProveedor.html"
		
		UserProveedorForm = UserProveedorCreateForm()
		PerfilProveedorForm = PerfilProveedorCreateForm()
		
		context = {
			'UserProveedorForm': UserProveedorForm,
			'PerfilProveedorForm': PerfilProveedorForm,
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name = "accounts/createProveedor.html"

		users = User.objects.filter(is_staff=False).count()
		userActual = users + 1

		NuevoUserForm = UserProveedorCreateForm(request.POST)
		NuevoPerfilForm = PerfilProveedorCreateForm(request.POST)
		
		if NuevoUserForm.is_valid(): 
			NuevoUser = NuevoUserForm.save(commit=False)
			NuevoUser.username = 'PROV' + str(NuevoUser.first_name[0].upper()) + str(NuevoUser.last_name[0].upper()) + str(userActual)
			NuevoUser.save()

		if NuevoPerfilForm.is_valid():
			NuevoPerfil = NuevoPerfilForm.save(commit=False)
			NuevoPerfil.user = NuevoUser
			NuevoPerfil.save()
		return redirect("accounts:ListViewTodos")

class profile(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/profile.html"
		return render(request,template_name)