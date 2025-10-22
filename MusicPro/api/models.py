from django.db import models
#from email.policy import default
from django.utils import timezone
#from django.contrib.auth.models import AbstractUser
#from django.contrib.auth import get_user_model
#User = get_user_model()
# Create your models here.


class Producto(models.Model):
    CATEGORIAS = (
        ('Instrumento de cuerda', (
            ('Guitarras', 'Guitarras'),
            ('Bajos', 'Bajos'),
            ('Pianos', 'Pianos')
        )),
        ('Percusion', (
            ('Baterias Acusticas', 'Baterias Acusticas'),
            ('Bateria Electronica', 'Bateria Electronica')
        )),
        ('Amplificadores', (
            ('Cabezales', 'Cabezales'),
            ('Cajas', 'Cajas')
        )),
        ('Accesorios varios', 'Accesorios varios')
    )

    categoria = models.CharField(max_length=25, choices=CATEGORIAS, null=True)
    marca = models.CharField(max_length=30)
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=35)
    valor = models.IntegerField()
    fecha = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='img', null=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class CarroProductos(models.Model):
    producto_id = models.IntegerField(default=0)
    nombre = models.CharField(max_length=35)
    total = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre


class Pedidos(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    valor_total = models.IntegerField()
    productos = models.ManyToManyField(CarroProductos)
    estado = models.CharField(max_length=25)

    def __str__(self):
        return self.estado


class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    comuna = models.CharField(max_length=60)
    region = models.CharField(max_length=80)
    depto = models.CharField(max_length=40)
    direccion_id = models.CharField(max_length=30)


class Cliente(models.Model):
    cliente_serie = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=10)
    correo = models.CharField(max_length=30)
    id_usuario = models.CharField(max_length=10)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
