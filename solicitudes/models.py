from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal
from presupuesto.models import Programa, Capitulo

class SolicitudRecursoFinanciero(models.Model):
	MetodoPago_CHOICES = {
		("CHEQUE", "CHEQUE"),
		("TRANSFERENCIA ELECTRÓNICA", "TRANSFERENCIA ELECTRÓNICA")
	}
	folio = models.CharField(max_length=10)
	programa = models.ForeignKey(Programa, related_name="programa", null=True, blank=True)
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

	class Meta:
		ordering = ['creacion']

	def __str__(self):
		return '{}'.format(self.folio)