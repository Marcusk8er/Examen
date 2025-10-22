import requests
from api.models import Pedidos, CarroProductos
from django.contrib.auth.models import User

class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            self.session['carro'] = {}
            self.carro = self.session['carro']
        else:
            self.carro = carro
    
    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carro.keys():
            self.carro[id]={
                "producto_id" : producto.id,
                "nombre" : producto.nombre,
                "acumulado" : producto.valor,
                "cantidad": 1,
            }
            c = CarroProductos(producto_id = producto.id, nombre= producto.nombre, total= producto.valor, cantidad=1)
            c.save()
        else:
            carroCompleto = CarroProductos.objects.all()
            self.carro[id]["cantidad"] += 1
            cont = self.carro[id]["cantidad"]
            productoEncontrado = carroCompleto.filter(producto_id = self.carro[id]["producto_id"])
            productoEncontrado.update(cantidad = cont)
            self.carro[id]["acumulado"] += producto.valor
            contValor = self.carro[id]["acumulado"]
            productoEncontrado = carroCompleto.filter(producto_id = self.carro[id]["producto_id"])
            productoEncontrado.update(total = contValor)
        
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True
        
    def eliminar(self, producto):
        id = str(producto.id)
        carroCompleto = CarroProductos.objects.all()
        if id in self.carro:
            productoEncontrado = carroCompleto.filter(producto_id = self.carro[id]["producto_id"])
            productoEncontrado.delete()
            del self.carro[id]
            self.guardar_carro()
    
    def restar(self, producto):
        id = str(producto.id)
        if id in self.carro.keys():
            carroCompleto = CarroProductos.objects.all()
            self.carro[id]["cantidad"] -= 1
            cont = self.carro[id]["cantidad"]
            productoEncontrado = carroCompleto.filter(producto_id = self.carro[id]["producto_id"])
            productoEncontrado.update(cantidad = cont)
            self.carro[id]["acumulado"] -= producto.valor
            contValor = self.carro[id]["acumulado"]
            productoEncontrado.update(total = contValor)
            if self.carro[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carro()
    
    def limpiar(self):
        self.session["carro"] = {}
        self.session.modified = True
        carroCompleto = CarroProductos.objects.all()
        carroCompleto.delete()
