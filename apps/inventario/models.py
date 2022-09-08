from django.db import models
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save

# Create your models here.

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    correo = models.EmailField(max_length=254, blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    productos = models.TextField(max_length=300, blank=True, null=True)
    ruc = models.CharField(max_length=13, blank=False, null=False, unique=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField('Codigo del producto', max_length=20, blank=False, null=False)
    repuesto = models.CharField('Tipo de repuesto',max_length=100, blank=False, null=False)
    cantidad = models.IntegerField('Cantidad de producto',blank=False, null=False)
    scant = models.IntegerField('Sumar cantidad', blank=False, null=False)
    rcant = models.IntegerField('Restar cantidad', blank=False, null=False)
    precioc = models.DecimalField('Precio de compra',max_digits=5, decimal_places=2, blank=False, null=False)
    preciov = models.DecimalField('Precio de venta',max_digits=5, decimal_places=2, blank=False, null=False)
    marca = models.CharField('Marca del repuesto',max_length=50, blank=True, null=True)
    ubicacion = models.CharField('Ubicación',max_length=50, blank=False, null=False)
    provedor_codigo = models.ManyToManyField(Proveedor)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['codigo']

    def __str__(self):
        return self.codigo

def quitar_relacion_proveedor(sender,instance,**kwargs):
    if instance.estado == False:
        proveedor = instance.id
        productos = Producto.objects.filter(provedor_codigo=proveedor)
        for producto in productos:
            producto.provedor_codigo.remove(proveedor)

post_save.connect(quitar_relacion_proveedor, sender= Proveedor)

class Pastilla(Producto):
    carro = models.CharField(max_length=200, blank=False, null=False)
    años = models.CharField(max_length=100, blank=False, null=False)
    posicion = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        verbose_name = 'Pastilla'
        verbose_name_plural = 'Pastillas'

    def __str__(self):
        return self.codigo

    def clean(self):
        if self.rcant >= self.cantidad:
            raise ValidationError('La cantidad a restar es mayor a la existente')
        if self.cantidad <1:
            raise ValidationError('Cantidad de producto baja')
        if self.scant == None:
            raise ValidationError('Ingrese un valor')
        if self.rcant == None:
            raise ValidationError('Ingrese un valor')

    def save(self,*args,**kwargs):
        self.cantidad = self.cantidad + self.scant
        self.cantidad = self.cantidad - self.rcant
        super(Pastilla,self).save(*args,**kwargs)

class Venta(models.Model):
    id = models.AutoField(primary_key= True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateField()
    cantidad = models.IntegerField(blank=False, null=False)
    total = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
