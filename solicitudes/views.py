from django.shortcuts import render
from django.views.generic import View 
from .models import *
from .forms import *

class ListViewSolicitudes(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = "solicitudes/listSolitudes.html"

		solicitudes = SolicitudRecursoFinanciero.objects.all()

		context = {
			'solicitudes': solicitudes,
		}
		return render(request,template_name,context)

class CreateViewSolicitud(View):
	def get(self, request):
		departamento = Departamento.objects.get(user=request.user)

		template_name = "solicitudes/createSolicitud.html"
				#form = ExcludedDateForm(departamento=departamento)
		form = SolicitudRecursoFinancieroCreateForm(departamento=departamento)

		context = {
		'departamento': departamento,
		'form': form,
		}

		return render(request,template_name,context)		