from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from accounts.models import Departamento, Banco

class Programa(models.Model):
	Fuente_CHOICES = (
		(1 , 'Federal'),
		(2 , 'Estatal'),
		(3 , 'Propios'),
	)
	nombre = models.CharField(max_length=150)
	departamento = models.ForeignKey(Departamento, null=True, blank=True)
	objetivo = models.TextField()
	actividad = models.TextField()
	meta = models.IntegerField()
	unidad_de_medida = models.CharField(max_length=50)
	fuente_de_financiamiento = models.IntegerField(choices=Fuente_CHOICES)
	beneficiarios = models.TextField()
	oficio_de_autorizacion = models.CharField(max_length=20)
	año = models.IntegerField()
	fecha_creado = models.DateTimeField(default=timezone.now)
	monto_anual_autorizado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_modificado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_ejercido = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_por_ejercer = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	cuenta_bancaria = models.CharField(max_length=150, null=True, blank=True)
	banco = models.ForeignKey(Banco, blank=True, null=True)

	def SacaPorcentaje(self):  
		self.pp = (self.monto_anual_ejercido*100)/self.monto_anual_autorizado
		self.save()

	def MontoAnualAutorizado(self):
		programa = Programa.objects.get(pk=self.pk)
		total_monto_autorizado_dict = Capitulo.objects.filter(programa=programa).aggregate(Sum('monto_anual_autorizado'))
		self.monto_anual_autorizado = total_monto_autorizado_dict['monto_anual_autorizado__sum']
		self.save()

	def MontoAnualAmpliacion(self):
		programa = Programa.objects.get(pk=self.pk)
		total_monto_ampliacion_dict = Capitulo.objects.filter(programa=programa).aggregate(Sum('monto_anual_ampliacion'))
		self.monto_anual_ampliacion = total_monto_ampliacion_dict['monto_anual_ampliacion__sum']
		self.save()

	def MontoAnualReduccion(self):
		programa = Programa.objects.get(pk=self.pk)
		total_monto_reduccion_dict = Capitulo.objects.filter(programa=programa).aggregate(Sum('monto_anual_reduccion'))
		self.monto_anual_reduccion = total_monto_reduccion_dict['monto_anual_reduccion__sum']
		self.save()

	def MontoAnualModificado(self):
		programa = Programa.objects.get(pk=self.pk)
		total_monto_modificado_dict = Capitulo.objects.filter(programa=programa).aggregate(Sum('monto_anual_modificado'))
		self.monto_anual_modificado = total_monto_modificado_dict['monto_anual_modificado__sum']
		self.save()

	def MontoAnualEjercido(self):
		programa = Programa.objects.get(pk=self.pk)
		total_monto_ejercido_dict = Capitulo.objects.filter(programa=programa).aggregate(Sum('monto_anual_ejercido'))
		self.monto_anual_ejercido = total_monto_ejercido_dict['monto_anual_ejercido__sum']
		self.save()

	def MontoAnualPorEjercer(self):
		programa = Programa.objects.get(pk=self.pk)
		total_monto_por_ejercer_dict = Capitulo.objects.filter(programa=programa).aggregate(Sum('monto_anual_por_ejercer'))
		self.monto_anual_por_ejercer = total_monto_por_ejercer_dict['monto_anual_por_ejercer__sum']
		self.save()

	def __str__(self):
		return self.nombre

class Capitulo(models.Model):

	Codigo_CHOICES = (
		(1000, '1000 - SERVICIOS PERSONALES'),
		(2000, '2000 - MATERIALES Y SUMINISTROS'),
		(3000, '3000 - SERVICIOS GENERALES'),
		(4000, '4000 - TRANSFERENCIAS, ASIGNACIONES, SUBSIDIOS Y OTRAS AYUDAS'),
		(5000, '5000 - BIENES MUEBLES, INMUEBLES E INTANGIBLES'),
		(6000, '6000 - INVERSIÓN PÚBLICA'),
		(7000, '7000 - INVERSIONES FINANCIERAS Y OTRAS PROVISIONES'),
		(8000, '8000 - PARTICIPACIONES Y APORTACIONES'),
		(9000, '9000 - DEUDA PÚBLICA'),
	)
	programa = models.ForeignKey(Programa)
	codigo = models.IntegerField(choices=Codigo_CHOICES)
	nombre = models.CharField(max_length=50)
	monto_anual_autorizado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_modificado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_ejercido = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_por_ejercer = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)

	def CreaNombre(self):
		if self.codigo==1000:
			self.nombre = 'SERVICIOS PERSONALES'
		elif self.codigo==2000:
			self.nombre = 'MATERIALES Y SUMINISTROS'
		elif self.codigo==3000:
			self.nombre = 'SERVICIOS GENERALES'
		elif self.codigo==4000:
			self.nombre = 'TRANSFERENCIAS, ASIGNACIONES, SUBSIDIOS Y OTRAS AYUDAS'
		elif self.codigo==5000:
			self.nombre = 'BIENES MUEBLES, INMUEBLES E INTANGIBLES'
		elif self.codigo==6000:
			self.nombre = 'INVERSIÓN PÚBLICA'
		elif self.codigo==7000:
			self.nombre = 'INVERSIONES FINANCIERAS Y OTRAS PROVISIONES'
		elif self.codigo==8000:
			self.nombre = 'PARTICIPACIONES Y APORTACIONES'
		elif self.codigo==9000:
			self.nombre = 'DEUDA PÚBLICA'
		self.save()

	def MontoAnualAutorizado(self):
		capitulo = Capitulo.objects.get(pk=self.pk)
		total_monto_anual_autorizado_dict = Partida.objects.filter(capitulo=capitulo).aggregate(Sum('monto_anual_autorizado'))
		self.monto_anual_autorizado = total_monto_anual_autorizado_dict['monto_anual_autorizado__sum']
		self.save()

	def MontoAnualAmpliacion(self):
		capitulo = Capitulo.objects.get(pk=self.pk)
		total_monto_anual_ampliacion_dict = Partida.objects.filter(capitulo=capitulo).aggregate(Sum('monto_anual_ampliacion'))
		self.monto_anual_ampliacion = total_monto_anual_ampliacion_dict['monto_anual_ampliacion__sum']
		self.save()

	def MontoAnualReduccion(self):
		capitulo = Capitulo.objects.get(pk=self.pk)
		total_monto_anual_reduccion_dict = Partida.objects.filter(capitulo=capitulo).aggregate(Sum('monto_anual_reduccion'))
		self.monto_anual_reduccion = total_monto_anual_reduccion_dict['monto_anual_reduccion__sum']
		self.save()

	def MontoAnualModificado(self):
		capitulo = Capitulo.objects.get(pk=self.pk)
		total_monto_anual_modificado_dict = Partida.objects.filter(capitulo=capitulo).aggregate(Sum('monto_anual_modificado'))
		self.monto_anual_modificado = total_monto_anual_modificado_dict['monto_anual_modificado__sum']
		self.save()

	def MontoAnualEjercido(self):
		capitulo = Capitulo.objects.get(pk=self.pk)
		total_monto_anual_ejercido_dict = Partida.objects.filter(capitulo=capitulo).aggregate(Sum('monto_anual_ejercido'))
		self.monto_anual_ejercido = total_monto_anual_ejercido_dict['monto_anual_ejercido__sum']
		self.save()

	def MontoAnualPorEjercer(self):
		capitulo = Capitulo.objects.get(pk=self.pk)
		total_monto_anual_por_ejercer_dict = Partida.objects.filter(capitulo=capitulo).aggregate(Sum('monto_anual_por_ejercer'))
		self.monto_anual_por_ejercer = total_monto_anual_por_ejercer_dict['monto_anual_por_ejercer__sum']
		self.save()
	def __str__(self):
		return '{} {}'.format(self.codigo, self.nombre)

class Partida(models.Model):
	capitulo = models.ForeignKey(Capitulo)
	codigo = models.IntegerField()
	descripcion = models.TextField()	
	#Montos anuales
	monto_anual_autorizado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_modificado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_ejercido = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_anual_por_ejercer = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)

	#Montos del primer trimestre
	monto_1t_autorizado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_1t_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_1t_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_1t_modificado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_1t_ejercido = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_1t_por_ejercer = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	
	#Montos del segundo trimestre
	monto_2t_autorizado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_2t_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_2t_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_2t_modificado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_2t_ejercido = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_2t_por_ejercer = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	
	#Montos del tercer trimestre
	monto_3t_autorizado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_3t_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_3t_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_3t_modificado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_3t_ejercido = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_3t_por_ejercer = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)

	#Montos del cuarto trimestre
	monto_4t_autorizado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_4t_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_4t_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_4t_modificado = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_4t_ejercido = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)
	monto_4t_por_ejercer = models.DecimalField(max_digits=20,decimal_places=2, default=0, null=True)

	#Calculos anuales
	def MontoAnualAutorizado(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_autorizado_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_autorizado'))
		self.monto_anual_autorizado = total_monto_autorizado_dict['monto_autorizado__sum']
		self.save()

	def MontoAnualAmpliacion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_ampliacion_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_ampliacion'))
		self.monto_anual_ampliacion = total_monto_ampliacion_dict['monto_ampliacion__sum']
		self.save()

	def MontoAnualReduccion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_reduccion_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_reduccion'))
		self.monto_anual_reduccion = total_monto_reduccion_dict['monto_reduccion__sum']
		self.save()

	def MontoAnualModificado(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_modificado_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_modificado'))
		self.monto_anual_modificado = total_monto_modificado_dict['monto_modificado__sum']
		self.save()

	def MontoAnualEjercido(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_ejercido_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_ejercido'))
		self.monto_anual_ejercido = total_monto_ejercido_dict['monto_ejercido__sum']
		self.save()

	def MontoAnualPorEjercer(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_por_ejercer_dict = Mes.objects.filter(partida=partida).aggregate(Sum('monto_por_ejercer'))
		self.monto_anual_por_ejercer = total_monto_por_ejercer_dict['monto_por_ejercer__sum']
		self.save()

#Calculos primer trimestre
	def Monto1TAutorizado(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_autorizado_dict = Mes.objects.filter(partida=partida, mes__gte=1, mes__lte=3).aggregate(Sum('monto_autorizado'))
		self.monto_1t_autorizado = total_monto_autorizado_dict['monto_autorizado__sum']
		self.save()

	def Monto1TAmpliacion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_ampliacion_dict = Mes.objects.filter(partida=partida, mes__gte=1, mes__lte=3).aggregate(Sum('monto_autorizado'))
		self.monto_1t_autorizado = total_monto_autorizado_dict['monto_autorizado__sum']
		self.save()

	def Monto1TAmpliacion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_ampliacion_dict = Mes.objects.filter(partida=partida, mes__gte=1, mes__lte=3).aggregate(Sum('monto_ampliacion'))
		self.monto_1t_ampliacion = total_monto_ampliacion_dict['monto_ampliacion__sum']
		self.save()

	def Monto1TReduccion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_reduccion_dict = Mes.objects.filter(partida=partida, mes__gte=1, mes__lte=3).aggregate(Sum('monto_reduccion'))
		self.monto_1t_reduccion = total_monto_reduccion_dict['monto_reduccion__sum']
		self.save()

	def Monto1TModificado(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_modificado_dict = Mes.objects.filter(partida=partida, mes__gte=1, mes__lte=3).aggregate(Sum('monto_modificado'))
		self.monto_1t_modificado = total_monto_modificado_dict['monto_modificado__sum']
		self.save()

	def Monto1TEjercido(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_ejercido_dict = Mes.objects.filter(partida=partida, mes__gte=1, mes__lte=3).aggregate(Sum('monto_ejercido'))
		self.monto_1t_ejercido = total_monto_ejercido_dict['monto_ejercido__sum']
		self.save()

	def Monto1TPorEjercer(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_por_ejercer_dict = Mes.objects.filter(partida=partida, mes__gte=1, mes__lte=3).aggregate(Sum('monto_por_ejercer'))
		self.monto_1t_por_ejercer = total_monto_por_ejercer_dict['monto_por_ejercer__sum']
		self.save()

#Calculos segundo trimestre
	def Monto2TAutorizado(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_autorizado_dict = Mes.objects.filter(partida=partida, mes__gte=4, mes__lte=6).aggregate(Sum('monto_autorizado'))
		self.monto_2t_autorizado = total_monto_autorizado_dict['monto_autorizado__sum']
		self.save()

	def Monto2TAmpliacion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_ampliacion_dict = Mes.objects.filter(partida=partida, mes__gte=4, mes__lte=6).aggregate(Sum('monto_autorizado'))
		self.monto_2t_autorizado = total_monto_autorizado_dict['monto_autorizado__sum']
		self.save()

	def Monto2TAmpliacion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_ampliacion_dict = Mes.objects.filter(partida=partida, mes__gte=4, mes__lte=6).aggregate(Sum('monto_ampliacion'))
		self.monto_2t_ampliacion = total_monto_ampliacion_dict['monto_ampliacion__sum']
		self.save()

	def Monto2TReduccion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_reduccion_dict = Mes.objects.filter(partida=partida, mes__gte=4, mes__lte=6).aggregate(Sum('monto_reduccion'))
		self.monto_2t_reduccion = total_monto_reduccion_dict['monto_reduccion__sum']
		self.save()

	def Monto2TModificado(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_modificado_dict = Mes.objects.filter(partida=partida, mes__gte=4, mes__lte=6).aggregate(Sum('monto_modificado'))
		self.monto_2t_modificado = total_monto_modificado_dict['monto_modificado__sum']
		self.save()

	def Monto2TEjercido(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_ejercido_dict = Mes.objects.filter(partida=partida, mes__gte=4, mes__lte=6).aggregate(Sum('monto_ejercido'))
		self.monto_2t_ejercido = total_monto_ejercido_dict['monto_ejercido__sum']
		self.save()

	def Monto2TPorEjercer(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_por_ejercer_dict = Mes.objects.filter(partida=partida, mes__gte=4, mes__lte=6).aggregate(Sum('monto_por_ejercer'))
		self.monto_2t_por_ejercer = total_monto_por_ejercer_dict['monto_por_ejercer__sum']
		self.save()

#Calculos tercer trimestre
	def Monto3TAutorizado(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_autorizado_dict = Mes.objects.filter(partida=partida, mes__gte=7, mes__lte=9).aggregate(Sum('monto_autorizado'))
		self.monto_3t_autorizado = total_monto_autorizado_dict['monto_autorizado__sum']
		self.save()

	def Monto3TAmpliacion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_ampliacion_dict = Mes.objects.filter(partida=partida, mes__gte=7, mes__lte=9).aggregate(Sum('monto_autorizado'))
		self.monto_3t_autorizado = total_monto_autorizado_dict['monto_autorizado__sum']
		self.save()

	def Monto3TAmpliacion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_ampliacion_dict = Mes.objects.filter(partida=partida, mes__gte=7, mes__lte=9).aggregate(Sum('monto_ampliacion'))
		self.monto_3t_ampliacion = total_monto_ampliacion_dict['monto_ampliacion__sum']
		self.save()

	def Monto3TReduccion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_reduccion_dict = Mes.objects.filter(partida=partida, mes__gte=7, mes__lte=9).aggregate(Sum('monto_reduccion'))
		self.monto_3t_reduccion = total_monto_reduccion_dict['monto_reduccion__sum']
		self.save()

	def Monto3TModificado(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_modificado_dict = Mes.objects.filter(partida=partida, mes__gte=7, mes__lte=9).aggregate(Sum('monto_modificado'))
		self.monto_3t_modificado = total_monto_modificado_dict['monto_modificado__sum']
		self.save()

	def Monto3TEjercido(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_ejercido_dict = Mes.objects.filter(partida=partida, mes__gte=7, mes__lte=9).aggregate(Sum('monto_ejercido'))
		self.monto_3t_ejercido = total_monto_ejercido_dict['monto_ejercido__sum']
		self.save()

	def Monto3TPorEjercer(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_por_ejercer_dict = Mes.objects.filter(partida=partida, mes__gte=7, mes__lte=9).aggregate(Sum('monto_por_ejercer'))
		self.monto_3t_por_ejercer = total_monto_por_ejercer_dict['monto_por_ejercer__sum']
		self.save()

#Calculos cuarto trimestre
	def Monto4TAutorizado(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_autorizado_dict = Mes.objects.filter(partida=partida, mes__gte=10, mes__lte=12).aggregate(Sum('monto_autorizado'))
		self.monto_4t_autorizado = total_monto_autorizado_dict['monto_autorizado__sum']
		self.save()

	def Monto4TAmpliacion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_ampliacion_dict = Mes.objects.filter(partida=partida, mes__gte=10, mes__lte=12).aggregate(Sum('monto_autorizado'))
		self.monto_4t_autorizado = total_monto_autorizado_dict['monto_autorizado__sum']
		self.save()

	def Monto4TAmpliacion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_ampliacion_dict = Mes.objects.filter(partida=partida, mes__gte=10, mes__lte=12).aggregate(Sum('monto_ampliacion'))
		self.monto_4t_ampliacion = total_monto_ampliacion_dict['monto_ampliacion__sum']
		self.save()

	def Monto4TReduccion(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_reduccion_dict = Mes.objects.filter(partida=partida, mes__gte=10, mes__lte=12).aggregate(Sum('monto_reduccion'))
		self.monto_4t_reduccion = total_monto_reduccion_dict['monto_reduccion__sum']
		self.save()

	def Monto4TModificado(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_modificado_dict = Mes.objects.filter(partida=partida, mes__gte=10, mes__lte=12).aggregate(Sum('monto_modificado'))
		self.monto_4t_modificado = total_monto_modificado_dict['monto_modificado__sum']
		self.save()

	def Monto4TEjercido(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_ejercido_dict = Mes.objects.filter(partida=partida, mes__gte=10, mes__lte=12).aggregate(Sum('monto_ejercido'))
		self.monto_4t_ejercido = total_monto_ejercido_dict['monto_ejercido__sum']
		self.save()

	def Monto4TPorEjercer(self):
		partida = Partida.objects.get(pk=self.pk)
		total_monto_por_ejercer_dict = Mes.objects.filter(partida=partida, mes__gte=10, mes__lte=12).aggregate(Sum('monto_por_ejercer'))
		self.monto_4t_por_ejercer = total_monto_por_ejercer_dict['monto_por_ejercer__sum']
		self.save()
	def __str__(self):
		return '{} {}'.format(self.codigo, self.descripcion)

class Mes(models.Model):	
	Mes_CHOICES = (
		(1 , 'Enero'),
		(2 , 'Febrero'),
		(3 , 'Marzo'),
		(4 , 'Abril'),
		(5 , 'Mayo'),
		(6 , 'Junio'),
		(7 , 'Julio'),
		(8 , 'Agosto'),
		(9 , 'Septiembre'),
		(10 , 'Octubre'),
		(11 , 'Noviembre'),
		(12 , 'Diciembre'),
	)
	partida = models.ForeignKey(Partida)
	mes = models.IntegerField(choices=Mes_CHOICES)
	monto_autorizado = models.DecimalField(max_digits=20,decimal_places=2)
	monto_ampliacion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_reduccion = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_modificado = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_ejercido = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	monto_por_ejercer = models.DecimalField(max_digits=20,decimal_places=2, default=0)
	
	def MontoModificado(self):
		self.monto_modificado = self.monto_autorizado + self.monto_ampliacion - self.monto_reduccion
		self.save()

	def MontoPorEjercer(self):
		self.monto_por_ejercer = self.monto_modificado - self.monto_ejercido
		self.save()

	def __str__(self):
		return '{} {}'.format(self.partida, self.mes)