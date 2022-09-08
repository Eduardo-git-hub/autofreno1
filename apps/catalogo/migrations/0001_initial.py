# Generated by Django 3.2 on 2022-09-01 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=100)),
                ('años', models.CharField(max_length=100)),
                ('posicion', models.CharField(max_length=200)),
                ('dimensionx', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('dimensiony', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('dimensionz', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('imagen', models.ImageField(max_length=200, upload_to='catalog/')),
                ('existencia', models.CharField(blank=True, choices=[('C', 'Con existencia'), ('S', 'Sin existencia')], max_length=1)),
            ],
            options={
                'verbose_name': 'Catalogo',
                'verbose_name_plural': 'Catalogos',
                'ordering': ['marca'],
            },
        ),
    ]