from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [

    path('listar_proveedor/',login_required(ListarProveedor.as_view()), name = 'listar_proveedor'),
    path('crear_proveedor/',login_required(CrearProveedor.as_view()), name = 'crear_proveedor'),
    path('editar_proveedor/<int:pk>/',login_required(ActualizarProveedor.as_view()), name = 'editar_proveedor'),
    path('elimininar_proveedor/<int:pk>/',login_required(EliminarProveedor.as_view()), name = 'elmininar_proveedor'),

    path('listar_pastilla/',login_required(ListarPastillas.as_view()), name = 'listar_pastilla'),
    path('crear_pastilla/',login_required(CrearPastillas.as_view()), name = 'crear_pastilla'),
    path('editar_pastilla/<int:pk>/',login_required(ActualizarPastillas.as_view()), name = 'editar_pastilla'),
    path('eliminar_pastilla/<int:pk>/',login_required(EliminarPastilla.as_view()), name = 'eliminar_pastilla'),
    path('reportes_productos/',login_required(Reportes_P.as_view()), name = 'reportes_productos'),
    path('reporte/',login_required(Report_P.as_view()), name = 'reporte')

]

"""
    path('crear_categoria/',login_required(CrearCategoria.as_view()), name = 'crear_categoria'),
    path('listar_categoria/',login_required(ListaCategoria.as_view()), name = 'listar_categoria'),
    path('editar_categoria/<int:pk>/',login_required(ActualizarCategoria.as_view()), name = 'editar_categoria'),
    path('eliminar_categoria/<int:pk>/',login_required(EliminarCategoria.as_view()), name = 'eliminar_categoria'),
"""
