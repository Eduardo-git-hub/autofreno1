from django import forms
from .models import Catalogo

class FormularioCatalogo(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = ['marca','modelo','años','posicion','dimensionx','dimensiony','dimensionz','imagen']
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'años': 'Años',
            'posicion': 'Posicion',
            'dimensionx': 'Valor x',
            'dimensiony': 'Valor y',
            'dimensionz': 'Valor z',
        }
        widgets = {
            'marca': forms.TextInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder':'Ingrese la marca del vehículo'
            }
            ),
            'modelo': forms.TextInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el modelo del vehiculo'
            }
            ),
            'años': forms.TextInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese los años permitidos'
            }
            ),
            'posicion': forms.TextInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la posición de la pieza',
                    'pattern': '[A-Z a-z]*',
                    'title': 'No se permiten números'
            }
            ),
            'dimensionx': forms.NumberInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'ingrese el valor de x',
                    'min': '0.1'
            }
            ),
            'dimensiony': forms.NumberInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'ingrese el valor de y',
                    'min': '0.1'
            }
            ),
            'dimensionz': forms.NumberInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'ingrese el valor de z',
                    'min': '0.1'
            }
            ),
        }
