from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^solicitudes/consultar/(?P<pk>\d+)/$', views.DetailViewSolicitudPropia.as_view(), name="DetailViewSolicitudPropia"),
	url(r'^solicitudes/por_pagar/consultar/(?P<pk>\d+)/$', views.DetailViewSolicitudPendiente.as_view(), name="DetailViewSolicitudPendiente"),
	url(r'^solicitudes/empleado/nuevo/$',views.CreateViewSolicitudEmpleado.as_view(), name='CreateViewSolicitudEmpleado'),
	url(r'^solicitudes/proveedor/nuevo/$',views.CreateViewSolicitudProveedor.as_view(), name='CreateViewSolicitudProveedor'),	
	url(r'^solicitudes/por_pagar/$',views.ListViewSolicitudesPendientes.as_view(), name='ListViewSolicitudesPendientes'),
	url(r'^solicitudes/$',views.ListViewSolicitudesPropias.as_view(), name='ListViewSolicitudesPropias'),
]