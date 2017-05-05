from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	#urls de empleados
#	url(r'^accounts/empleado/desactivar/(?P<pk>\d+)/$', views.DesactivateViewUser.as_view(), name="DesactivateViewUser"),
	url(r'^accounts/director/actualizar/(?P<pk>\d+)/$', views.UpdateViewDirector.as_view(), name="UpdateViewDirector"),
	url(r'^accounts/director/nuevo/$',views.CreateViewDirector.as_view(), name='CreateViewDirector'),
	url(r'^accounts/directores/$',views.ListViewDirectores.as_view(), name='ListViewDirectores'),

	#urls de empleados
	url(r'^accounts/empleado/desactivar/(?P<pk>\d+)/$', views.DesactivateViewUser.as_view(), name="DesactivateViewUser"),
	url(r'^accounts/empleado/actualizar/(?P<pk>\d+)/$', views.UpdateViewEmpleado.as_view(), name="UpdateViewEmpleado"),
	url(r'^accounts/empleado/nuevo/$',views.CreateViewEmpleado.as_view(), name='CreateViewEmpleado'),
	url(r'^accounts/empleados/$',views.ListViewEmpleados.as_view(), name='ListViewEmpleados'),

	#urls de proveedores
	url(r'^accounts/proveedor/actualizar/(?P<pk>\d+)/$', views.UpdateViewProveedor.as_view(), name="UpdateViewProveedor"),
	url(r'^accounts/proveedor/nuevo/$',views.CreateViewProveedor.as_view(), name='CreateViewProveedor'),
	url(r'^accounts/proveedores/$',views.ListViewProveedores.as_view(), name='ListViewProveedores'),

	#urls de bancos
	url(r'^accounts/bancos/actualizar/(?P<pk>\d+)$',views.UpdateViewBanco.as_view(), name='UpdateViewBanco'),
	url(r'^accounts/bancos/eliminar/(?P<pk>\d+)$',views.DeleteViewBanco.as_view(), name='DeleteViewBanco'),
	url(r'^accounts/bancos/nuevo/$',views.CreateViewBanco.as_view(), name='CreateViewBanco'),	
	url(r'^accounts/bancos/$',views.ListViewBancos.as_view(), name='ListViewBancos'),
	
	#urls de departamentos
	url(r'^accounts/departamentos/actualizar/(?P<pk>\d+)$',views.UpdateViewDepartamento.as_view(), name='UpdateViewDepartamento'),
	url(r'^accounts/departamentos/eliminar/(?P<pk>\d+)$',views.DeleteViewDepartamento.as_view(), name='DeleteViewDepartamento'),
	url(r'^accounts/departamentos/nuevo/$',views.CreateViewDepartamento.as_view(), name='CreateViewDepartamento'),	
	url(r'^accounts/departamentos/$',views.ListViewDepartamentos.as_view(), name='ListViewDepartamentos'),


	#url de perfil
	url(r'^accounts/profile/$',views.profile.as_view(), name='profile'),
	
	#url de login y logout
	url(r'^login', login,name="login"),
	url(r'^logout/$', logout, name="logout"),
]