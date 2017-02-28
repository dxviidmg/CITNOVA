from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^solicitudes/nuevo/$',views.CreateViewSolicitud.as_view(), name='CreateViewSolicitud'),
	url(r'^solicitudes/$',views.ListViewSolicitudes.as_view(), name='ListViewSolicitudes'),
]