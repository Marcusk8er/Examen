from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import CarroProductos, Pedidos, Producto

class UserSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProductoSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Producto
        fields = ['url', 'id', 'categoria', 'nombre', 'marca', 'codigo', 'valor', 'fecha', 'img', 'stock']

class CarroProductosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarroProductos
        fields = ['producto_id', 'nombre', 'total', 'cantidad']

class PedidosSerializer(serializers.HyperlinkedModelSerializer) :
    productos = CarroProductosSerializer(read_only=True, many=True)
    class Meta:
        model = Pedidos
        fields = ['url','nombre_usuario', 'valor_total', 'productos', 'estado']