from django.conf.urls import url
from . import views


urlpatterns = [
	
	url(r'^programas/capitulos/partidas/meses/actualizar/ampliacion/(?P<pk>\d+)/$', views.UpdateViewMesAmpliacion.as_view(), name="UpdateViewMesAmpliacion"),
	url(r'^programas/capitulos/partidas/meses/actualizar/reduccion/(?P<pk>\d+)/$', views.UpdateViewMesReduccion.as_view(), name="UpdateViewMesReduccion"),
	url(r'^programas/capitulos/partidas/meses/actualizar/ejercido/(?P<pk>\d+)/$', views.UpdateViewMesEjercido.as_view(), name="UpdateViewMesEjercido"),

	url(r'^programas/capitulos/partidas/meses/nuevo/(?P<pk>\d+)/$', views.CreateViewMes.as_view(), name="CreateViewMes"),
	url(r'^programas/capitulos/partidas/meses/actualizar/(?P<pk>\d+)/$', views.UpdateViewMes.as_view(), name="UpdateViewMes"),
	url(r'^programas/capitulos/partidas/meses/eliminar/(?P<pk>\d+)/$', views.DeleteViewMes.as_view(), name="DeleteViewMes"),
	url(r'^programas/capitulos/partidas/meses/(?P<pk>\d+)/$', views.ListViewMeses.as_view(), name="ListViewMeses"),

	url(r'^programas/capitulos/partidas/nuevo/(?P<pk>\d+)/$', views.CreateViewPartida.as_view(), name="CreateViewPartida"),
	url(r'^programas/capitulos/partidas/actualizar/(?P<pk>\d+)/$', views.UpdateViewPartida.as_view(), name="UpdateViewPartida"),
	url(r'^programas/capitulos/partidas/eliminar/(?P<pk>\d+)/$', views.DeleteViewPartida.as_view(), name="DeleteViewPartida"),
	url(r'^programas/capitulos/partidas/(?P<pk>\d+)/$', views.ListViewPartidas.as_view(), name="ListViewPartidas"),

	url(r'^programas/capitulos/nuevo/(?P<pk>\d+)/$', views.CreateViewCapitulo.as_view(), name="CreateViewCapitulo"),
	url(r'^programas/capitulos/actualizar/(?P<pk>\d+)/$', views.UpdateViewCapitulo.as_view(), name="UpdateViewCapitulo"),
	url(r'^programas/capitulos/eliminar/(?P<pk>\d+)/$', views.DeleteViewCapitulo.as_view(), name="DeleteViewCapitulo"),
	url(r'^programas/capitulos/(?P<pk>\d+)/$', views.ListViewCapitulos.as_view(), name="ListViewCapitulos"),
	
	url(r'^programas/nuevo/$', views.CreateViewPrograma.as_view(), name="CreateViewPrograma"),
	url(r'^programas/actualizar/(?P<pk>\d+)/$', views.UpdateViewPrograma.as_view(), name="UpdateViewPrograma"),
	url(r'^programas/eliminar/(?P<pk>\d+)/$', views.DeleteViewPrograma.as_view(), name="DeleteViewPrograma"),
	url(r'^programas/$',views.ListViewProgramas.as_view(),name='ListViewProgramas'),

]