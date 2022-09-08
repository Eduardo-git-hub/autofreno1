from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.usuario.views import ListarUsuario,RegistrarUsuario,EditarUsuario,EliminarUsuario

urlpatterns = [
    path('listado_usuarios/',login_required(ListarUsuario.as_view()), name = 'listar_usuarios'),
    path('registar_usuario/',login_required(RegistrarUsuario.as_view()), name = 'crear_usuario'),
    path('editar_usuario/<int:pk>/',login_required(EditarUsuario.as_view()), name = 'editar_usuario'),
    path('eliminar_usuario/<int:pk>/',login_required(EliminarUsuario.as_view()), name = 'eliminar_usuario')
]
