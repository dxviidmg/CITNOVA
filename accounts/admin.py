from django.contrib import admin
from .models import *
from .forms import *
#from django.forms.models import inlineformset_factory
#from django.contrib.auth.models import User

#class MyUserAdmin(admin.ModelAdmin):
#	form = UserModelForm

admin.site.register(Perfil)
admin.site.register(Departamento)
admin.site.register(Banco)
admin.site.register(Expediente)

#admin.site.unregister(User)
#admin.site.register(User, MyUserAdmin)

#from django.contrib.auth.admin import UserAdmin

#UserAdmin.list_display += ('departamento',)  # don't forget the commas
#UserAdmin.list_filter += ('departamento',)
#UserAdmin.fieldsets += ('departamento',)