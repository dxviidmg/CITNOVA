from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal

class SolicitudRecursoFinanciero(models.Model):
	MetodoPago_CHOICES = {
		("CHEQUE", "CHEQUE"),
		("TRANSFERENCIA ELECTRÓNICA", "TRANSFERENCIA ELECTRÓNICA")
	}
	folio = models.CharField(max_length=10)
	a_nombre_de = models.ForeignKey(User, related_name="a_nombre_de")
	concepto = models.CharField(max_length=100)
	importe_numero = models.DecimalField(max_digits=20,decimal_places=2)
	importe_letra = models.CharField(max_length=100)
	metodo_pago = models.CharField(max_length=30, choices= MetodoPago_CHOICES)
	clabe = models.CharField(max_length=100)
	creacion = models.DateTimeField(default=timezone.now)
	solicitante = models.ForeignKey(User, null=True, related_name="solicitante")

	class Meta:
		ordering = ['folio']

	def __str__(self):
		return '{}'.format(self.folio)