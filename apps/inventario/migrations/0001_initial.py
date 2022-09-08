# Generated by Django 3.2 on 2022-09-01 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=20, verbose_name='Codigo del producto')),
                ('repuesto', models.CharField(max_length=100, verbose_name='Tipo de repuesto')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad de producto')),
                ('scant', models.IntegerField(verbose_name='Sumar cantidad')),
                ('rcant', models.IntegerField(verbose_name='Restar cantidad')),
                ('precioc', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Precio de compra')),
                ('preciov', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Precio de venta')),
                ('marca', models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca del repuesto')),
                ('ubicacion', models.CharField(max_length=50, verbose_name='Ubicación')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('productos', models.TextField(blank=True, max_length=300, null=True)),
                ('ruc', models.CharField(max_length=13, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pastilla',
            fields=[
                ('producto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventario.producto')),
                ('carro', models.CharField(max_length=200)),
                ('años', models.CharField(max_length=100)),
                ('posicion', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Pastilla',
                'verbose_name_plural': 'Pastillas',
            },
            bases=('inventario.producto',),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cliente', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='provedor_codigo',
            field=models.ManyToManyField(to='inventario.Proveedor'),
        ),
    ]
