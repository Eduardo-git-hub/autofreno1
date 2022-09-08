import django_filters
from .models import Catalogo

class catalogfilter (django_filters.FilterSet):

    class Meta:
        model = Catalogo
        fields = {
            'marca': ['icontains'],
            'modelo': ['icontains']
        }
