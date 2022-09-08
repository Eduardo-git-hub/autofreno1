from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('listar_catalogo/',login_required(ListarCat.as_view()), name = 'listar_catalogo'),
    path('crear_catalogo/',login_required(CrearCat.as_view()), name = 'crear_catalogo'),
    path('editar_catalogo/<int:pk>/',login_required(ActualizarCat.as_view()), name = 'editar_catalogo'),
    path('eliminar_catalogo/<int:pk>/',login_required(EliminarCat.as_view()), name = 'eliminar_catalogo')
]
