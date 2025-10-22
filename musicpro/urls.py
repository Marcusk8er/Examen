"""musicpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from musicpro.app_api import views
from django.conf.urls.static import static
from django.conf import settings
from tienda.views import agregar_producto, api_dolar, eliminar_producto, limpiar_carro, pedido, productos, restar_producto, index
from api.views import registro
from django.contrib.auth.views import LoginView, LogoutView

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

router.register(r'productos', views.ProductoViewSet)
router.register(r'pedidos', views.PedidosViewSet)
router.register(r'carroProductos', views.CarroProductosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', 
        namespace='rest_framework')),
    path('', index, name='index'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('productos/', productos, name='productos'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carro, name="CLS"),
    path('carro/', api_dolar, name='carro'),
    path('pedido/', pedido, name='pedido'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('registrarse/', registro, name='registrarse')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
