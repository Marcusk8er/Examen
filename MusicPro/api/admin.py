from django.contrib import admin
from tienda.models import Usuarios

from django.contrib.auth.admin import UserAdmin
from .forms import Registro
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = Usuarios
    add_form = Registro

    fieldset = (
        *UserAdmin.fieldsets,
        (
            'User information', {
                'fields': (
                    'is_contador',
                    'is_bodeguero',
                    'is_cliente',
                    'is_vendedor',
                    'comuna',
                    'calle',
                    'celular'
                )
            }
        )
    )


admin.site.register(Usuarios, CustomUserAdmin)
