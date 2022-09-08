from django.contrib import admin
from apps.catalogo.models import Catalogo
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CatalogoResource(resources.ModelResource):
    class Meta:
        model = Catalogo

class CatalogoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['marca']
    list_display = ('marca','modelo','años','posicion','dimensionx','dimensiony','dimensionz','imagen')
    resource_class = CatalogoResource

admin.site.register(Catalogo,CatalogoAdmin)
