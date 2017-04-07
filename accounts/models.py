from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Departamento(models.Model):
	nombre = models.CharField(max_length=100)
	codigo = models.CharField(max_length=10)
	
	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['nombre']

class Banco(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['nombre']

class Perfil(models.Model):
	
	GradoProfesional_CHOICES = {
		("Tec.", "Tec."),
		("T. S. U.", "T. S. U."),
		("Lic.", "Lic."),
		("Arq.", "Arq."),
		("Ing.", "Ing."),
		("Mtro(a).", "Mtro(a)."),
		("Dr.", "Dr.")
	}

	user = models.OneToOneField(User)
	grado_profesional = models.CharField(max_length=30, choices=GradoProfesional_CHOICES, blank=True, default="C.")
	puesto = models.CharField(max_length=30, blank=True, null=True)
	telefono = models.CharField(max_length=10, blank=True, null=True)
	banco = models.ForeignKey(Banco, blank=True, null=True)
	cuenta_bancaria = models.CharField(max_length=16, blank=True, null=True)
	CLABE = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return '{} {}'.format(self.user.last_name, self.user.first_name)

	class Meta:
		ordering = ['user']

class Expediente(models.Model):
	Tipo_CHOICES = {
		("P. Física", "P. Física"),
		("P. Moral", "P. Moral"),
	}

	perfil = models.OneToOneField(Perfil)
	tipo = models.CharField(max_length=20, choices=Tipo_CHOICES)
	RFC = models.FileField(upload_to='Expedientes/%Y/%m/%d/', null=True, blank=True)
	IFE = models.ImageField(upload_to='IFE/%Y/%m/%d/', null=True, blank=True)
		
	def __str__(self):
		return 'Expediente de {}'.format(self.perfil)

User.add_to_class('departamento', models.ForeignKey(Departamento, blank = True, null=True))

def get_first_name(self):
#    return self.first_name
	return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_first_name)