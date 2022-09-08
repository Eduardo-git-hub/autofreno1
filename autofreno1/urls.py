"""autofreno1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from apps.inventario.views import Inicio
from apps.catalogo.views import Catalog,About
from apps.usuario.views import Login,logoutUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include(('apps.usuario.urls','usuarios'))),
    path('inventario/', include(('apps.inventario.urls','inventario'))),
    path('catalogo/', include(('apps.catalogo.urls','catalogo'))),
    path('catalogo', Catalog.as_view(), name= 'catalogo'),
    path('', About.as_view(), name= 'about'),
    path('inicio/', login_required(Inicio.as_view()), name = 'index'),
    path('accounts/login/', Login.as_view(), name = 'login'),
    path('logout', login_required(logoutUsuario), name = 'logout')
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT,})
]
