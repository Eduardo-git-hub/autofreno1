from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import FormularioCatalogo
from .models import Catalogo
from .filters import catalogfilter

# Create your views here.

class Catalog(ListView):
    model = Catalogo
    template_name = 'catalogovista.html'
    paginate_by = 12

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qu = self.request.GET.get('q')
        de = self.request.GET.get('d')
        if qu:
            return qs.filter(marca__icontains = qu)
        if de:
            return qs.filter(modelo__icontains = de)
        return qs

class ListarCat(ListView):
    model = Catalogo
    paginate_by = 12
    template_name = 'catalogo/listar_catalogo.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        bmarca = self.request.GET.get('filtrarm')
        bcódigo = self.request.GET.get('filtrarc')
        if bmarca:
            return qs.filter(marca__icontains = bmarca)
        if bcódigo:
            return qs.filter(modelo__icontains = bcódigo)
        return qs

class CrearCat(CreateView):
    model = Catalogo
    form_class = FormularioCatalogo
    template_name = 'catalogo/crear_catalogo.html'

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('catalogo:listar_catalogo')

class ActualizarCat(UpdateView):
    model = Catalogo
    form_class = FormularioCatalogo
    template_name = 'catalogo/crear_catalogo.html'
    success_url = reverse_lazy('catalogo:listar_catalogo')

class EliminarCat(DeleteView):
    model = Catalogo
    success_url = reverse_lazy('catalogo:listar_catalogo')


class About(TemplateView):
    template_name = 'about.html'
