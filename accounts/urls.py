from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^login', login,name="login"),
	url(r'^logout/$', logout, name="logout"),
	url(r'^accounts/empleado/nuevo/$',views.CreateViewEmpleado.as_view(), name='CreateViewEmpleado'),
	url(r'^accounts/empleado/actualizar/(?P<pk>\d+)/$', views.UpdateViewEmpleado.as_view(), name="UpdateViewEmpleado"),

	url(r'^accounts/proveedor/nuevo/$',views.CreateViewProveedor.as_view(), name='CreateViewProveedor'),
	url(r'^accounts/proveedor/actualizar/(?P<pk>\d+)/$', views.UpdateViewProveedor.as_view(), name="UpdateViewProveedor"),

	url(r'^accounts/empleados/$',views.ListViewEmpleados.as_view(), name='ListViewEmpleados'),
	url(r'^accounts/proveedores/$',views.ListViewProveedores.as_view(), name='ListViewProveedores'),
	url(r'^accounts/profile/$',views.profile.as_view(), name='profile'),
]