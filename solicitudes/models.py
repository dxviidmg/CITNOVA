from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal
from presupuesto.models import Mes

class SolicitudRecursoFinanciero(models.Model):
	MetodoPago_CHOICES = {
		("CHEQUE", "CHEQUE"),
		("TRANSFERENCIA ELECTRÓNICA", "TRANSFERENCIA ELECTRÓNICA")
	}
	folio = models.CharField(max_length=10)
	mes = models.ForeignKey(Mes, null=True, blank=True)
	a_nombre_de = models.ForeignKey(User, related_name="a_nombre_de")
	concepto = models.TextField()
	importe_numero = models.DecimalField(max_digits=20,decimal_places=2)
	importe_letra = models.CharField(max_length=100)
	metodo_pago = models.CharField(max_length=30, choices= MetodoPago_CHOICES)
	clabe = models.CharField(max_length=100)
	creacion = models.DateTimeField(default=timezone.now)
	solicitante = models.ForeignKey(User, related_name="solicitante")
	pagado = models.BooleanField(default=False)
	comprobante = models.FileField(upload_to='Comprobantes/%Y/%m/%d/', null=True, blank=True)
	fecha_pagado = models.DateTimeField(blank=True, null=True)
	cuenta_bancaria_del_programa = models.CharField(max_length=30,  null=True, blank=True)
	class Meta:
		ordering = ['creacion']

	def __str__(self):
		return '{}'.format(self.folio)

	def FechaPagado(self):
		if self.pagado==True:
			self.fecha_pagado = timezone.now()
			self.save()