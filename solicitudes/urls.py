from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^solicitudes/empleado/nuevo/$',views.CreateViewSolicitudEmpleado.as_view(), name='CreateViewSolicitudEmpleado'),
	url(r'^solicitudes/proveedor/nuevo/$',views.CreateViewSolicitudProveedor.as_view(), name='CreateViewSolicitudProveedor'),	
	url(r'^solicitudes/$',views.ListViewSolicitudes.as_view(), name='ListViewSolicitudes'),
]