from django.contrib import admin
from .models import *
#from .forms import *
#from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User

admin.site.register(Perfil)
admin.site.register(Departamento)
admin.site.register(Banco)

from django.contrib.auth.admin import UserAdmin

UserAdmin.list_display += ('departamento',)  # don't forget the commas
UserAdmin.list_filter += ('departamento',)
#UserAdmin.fieldsets += ('departamento',)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserProfileInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfil'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)