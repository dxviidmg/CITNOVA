from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^solicitudes/search/$',views.SearchSolicitudes.as_view(), name='SearchSolicitudes'),

	#Urls de detalla de solicitudes 
	url(r'^solicitudes/consultar/propias/(?P<pk>\d+)/$', views.DetailViewSolicitudPropia.as_view(), name="DetailViewSolicitudPropia"),
	url(r'^solicitudes/consultar/ajenas/(?P<pk>\d+)/$', views.DetailViewSolicitudPendiente.as_view(), name="DetailViewSolicitudPendiente"),
	url(r'^solicitudes/por_mes/(?P<pk>\d+)/$', views.ListViewSolicitudesPorMes.as_view(), name="ListViewSolicitudesPorMes"),

	#Urls de creación de solicitudes
	url(r'^solicitudes/empleado/nuevo/$',views.CreateViewSolicitudEmpleado.as_view(), name='CreateViewSolicitudEmpleado'),
	url(r'^solicitudes/proveedor/nuevo/$',views.CreateViewSolicitudProveedor.as_view(), name='CreateViewSolicitudProveedor'),	
	
	#Urls de listas de solicitudes
	url(r'^solicitudes/por_pagar/$',views.ListViewSolicitudesPendientes.as_view(), name='ListViewSolicitudesPendientes'),
	url(r'^solicitudes/pagadas/$',views.ListViewSolicitudesPagadas.as_view(), name='ListViewSolicitudesPagadas'),
	url(r'^solicitudes/$',views.ListViewSolicitudesPropias.as_view(), name='ListViewSolicitudesPropias'),

]