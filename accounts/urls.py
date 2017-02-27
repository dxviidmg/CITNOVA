from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^login', login,name="login"),
	url(r'^logout/$', logout, name="logout"),
	url(r'^accounts/empleado/nuevo/$',views.CreateViewEmpleado.as_view(), name='CreateViewEmpleado'),
	url(r'^accounts/proveedor/nuevo/$',views.CreateViewProveedor.as_view(), name='CreateViewProveedor'),
	url(r'^accounts/$',views.ListViewTodos.as_view(), name='ListViewTodos'),
	url(r'^accounts/profile/$',views.profile.as_view(), name='profile'),
]