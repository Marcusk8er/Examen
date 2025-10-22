from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Usuarios(AbstractUser):
    is_cliente = models.BooleanField('Is cliente', default=False)
    is_vendedor = models.BooleanField('Is vendedor', default=False)
    is_bodeguero = models.BooleanField('Is bodeguero', default=False)
    is_contador = models.BooleanField('Is contador', default=False)
    celular = models.CharField('celular', max_length=9, blank=True, null=True)
    comuna = models.CharField('comuna', max_length=255, blank=True, null=True)
    calle = models.CharField('calle', max_length=255, blank=True, null=True)
    email = models.CharField('email', max_length=150, unique=True, null=True)
    REQUIRED_FIELDS = ['USERNAME']
    USERNAME_FIELD = "email"
