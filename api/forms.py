
from django.contrib.auth.forms import UserCreationForm
from django import forms

from tienda.models import Usuarios


class Registro(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['username', 'password', 'password2']


class Clientes(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ('username', 'email', 'password',
                  'password2', 'comuna', 'calle', 'celular')
        labels = {
            'username': 'Nombre del usuario',
            'email': 'Email',
            'password': 'Contraseña',
            'password2': 'Confirme su contraseña',
            'comuna': 'Comuna o Ciudad',
            'calle': 'Calle',
            'celular': 'celular'
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de usuario',
                    'id': 'username'
                }
            ),
            'primer_nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido',
                    'id': 'apellido'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Corre electronico',
                    'id': 'email'
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su contraseña',
                    'id': 'contraseña'
                }
            ),
            'password2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirme su contraseña',
                    'id': 'contraseña2'
                }
            ),
            'comuna': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su comuna',
                    'id': 'comuna'
                }
            ),
            'calle': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su calle',
                    'id': 'calle'
                }
            ),
            'celular': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su celular o teléfono',
                    'id': 'celular'
                }
            )}
