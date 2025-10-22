from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from musicpro.app_api.serializers import CarroProductosSerializer, PedidosSerializer,Pedidos, Producto, ProductoSerializer, UserSerializer, GroupSerializer
from api.models import CarroProductos, Pedidos, Producto

# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated] 

class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer
    permission_classes = [permissions.IsAuthenticated]

class CarroProductosViewSet(viewsets.ModelViewSet):
    queryset = CarroProductos.objects.all()
    serializer_class = CarroProductosSerializer
    permission_classes = [permissions.IsAuthenticated]

#Vista Usuarios
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
