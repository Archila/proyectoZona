from django.conf.urls import include, url
from . import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.inicio, name='index'),
    url(r'^productos/$', views.lista_productos, name='url_productos'),
    url(r'^proveedores/$', views.lista_proveedores, name='url_proveedores'),
    url(r'^proyectos/$', views.lista_productos, name='url_proyectos'),
    url(r'^nuevo/$', views.nuevo_proyecto, name='url_nuevo'),

    url(r'^/productos/nuevo/$', views.nuevo_producto, name='url_nuevo_producto'),
    url(r'^/productos/editar/(?P<pk>[0-9]+)/$', views.editar_producto, name='url_editar_producto'),
    url(r'^/productos/eliminar/(?P<pk>[0-9]+)/$', views.eliminar_producto, name='url_eliminar_producto'),
    url(r'^/productos/actualizar/(?P<pk>[0-9]+)/$', views.actualizar_producto, name='url_actualizar_producto'),
    url(r'^/productos/insert/$', views.insertar_producto, name='url_insertar_producto'),

    url(r'^/proveedores/nuevo/$', views.nuevo_proveedor, name='url_nuevo_proveedor'),
    url(r'^/proveedores/editar/(?P<pk>[0-9]+)/$', views.editar_proveedor, name='url_editar_proveedor'),
    url(r'^/proveedores/eliminar/(?P<pk>[0-9]+)/$', views.eliminar_proveedor, name='url_eliminar_proveedor'),
    url(r'^/proveedores/actualizar/(?P<pk>[0-9]+)/$', views.actualizar_proveedor, name='url_actualizar_proveedor'),
    url(r'^/proveedores/insert/$', views.insertar_proveedor, name='url_insertar_proveedor'),
]
