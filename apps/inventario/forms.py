from django import forms
from .models import Proveedor, Pastilla

"""
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre','ubicacion','descipcion','estado']
        labels = {
            'nombre': 'Nombre de la categoría',
            'ubicacion': 'Lugar de almacenamiento',
            'descipcion': 'Descripción',
            'estado': 'Activo/No Activo'
        }
        widgets = {
            'nombre': forms.TextInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder':'Ingrese el nombre de la categoria'
            }
            ),
            'ubicacion': forms.TextInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la ubicación fisica de almacenamiento'
            }
            ),
            'descipcion': forms.Textarea(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese una pequeña descripción'
            }
            ),
        }
"""
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','correo','telefono','productos','ruc','direccion']
        labels = {
            'nombre': 'Nombre',
            'correo': 'Email',
            'telefono': 'Teléfono/Celular',
            'productos': 'Productos que oferta',
            'ruc': 'RUC',
            'direccion': 'Dirección',
        }
        widgets = {
            'nombre': forms.TextInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese un nombre ej.(Marco)',
            'pattern': '[A-Z a-z]*',
            'title': 'No se permiten números'
            }
            ),
            'correo': forms.EmailInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese un email ej.(ejemplo@hotmail.com)'
            }
            ),
            'telefono': forms.TextInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese un número de teléfono/celular',
            'pattern': '\+?1?\d{10}',
            'title': 'Ingrese solo números y 10 dígitos'
            }
            ),
            'productos': forms.Textarea(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese los productos que ofrece el proveedor'
            }
            ),
            'ruc': forms.TextInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese el RUC del proveedor',
            'pattern': '\+?1?\d{13}',
            'title': 'Ingrese solo números y 13 dígitos'
            }
            ),
            'direccion': forms.TextInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese la dirección del proveedor'
            }
            ),
        }

class PastillaForm(forms.ModelForm):
    class Meta:
        model = Pastilla
        fields = ['codigo','repuesto','cantidad','scant','rcant','precioc','preciov','marca','ubicacion','provedor_codigo','carro','años','posicion']
        labels = {
            'codigo': 'Código',
            'repuesto': 'Tipo de repuesto',
            'cantidad': 'Cantidad',
            'scant': 'Sumar cant',
            'rcant': 'Restar cant',
            'precioc': 'Precio de compra',
            'preciov': 'Precio de venta',
            'marca': 'Marca del producto',
            'ubicacion': 'Almacenamiento',
            'provedor_codigo': 'Proveedor',
            'carro': 'Vehiculo al que pertenece',
            'años': 'Años permitidos',
            'posicion': 'Posicion de la pieza'
        }
        widgets = {
            'codigo': forms.TextInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese el código de producto'
            }
            ),
            'repuesto': forms.TextInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Indique el tipo de producto',
            'max_length': '100',
            'pattern': '[A-Z a-z]*',
            'title': 'No se permiten números'
            }
            ),
            'cantidad': forms.NumberInput(
            attrs = {
            'class': 'form-control',
            'min': '0'
            }
            ),
            'scant': forms.NumberInput(
            attrs = {
            'class': 'form-control',
            'min': '0',
            }
            ),
            'rcant': forms.NumberInput(
            attrs = {
            'class': 'form-control',
            'min': '0',
            }
            ),
            'precioc': forms.NumberInput(
            attrs = {
            'class': 'form-control',
            'min': '0.01'
            }
            ),
            'preciov': forms.NumberInput(
            attrs = {
            'class': 'form-control',
            'min': '0.01'
            }
            ),
            'marca': forms.TextInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese la marca del producto',
            'pattern': '[A-Z a-z]*',
            'title': 'No se permiten números'
            }
            ),
            'ubicacion': forms.TextInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese la ubicación de almacenamiento(ejemplo"Stock")',
            }
            ),
            'provedor_codigo': forms.SelectMultiple(
            attrs = {
            'class': 'form-control',
            }
            ),
            'carro': forms.TextInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese los carror compatibles',
            'autocomplete': 'off',
            'pattern': '[A-Z a-z]*',
            'title': 'No se permiten números'
            }
            ),
            'años': forms.TextInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese los años permitidos',
            'autocomplete': 'off'
            }
            ),
            'posicion': forms.TextInput(
            attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese la posicion de la pieza',
            'autocomplete': 'off',
            'pattern': '[A-Z a-z]*',
            'title': 'No se permiten números'
            }
            )
        }
