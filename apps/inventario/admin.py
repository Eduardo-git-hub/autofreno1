from django.contrib import admin
from .models import Pastilla,Proveedor,Producto,Venta
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Pastilla)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Venta)
