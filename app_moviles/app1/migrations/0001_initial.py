# Generated by Django 5.1 on 2024-12-03 23:20

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especies_app',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('geom_wkb', models.BinaryField()),
                ('fid', models.BigIntegerField()),
                ('cuadricula', models.CharField(max_length=50)),
                ('grupo', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('especie', models.CharField(max_length=50)),
                ('nombre_cientifico', models.CharField(max_length=50)),
                ('nombre_comun', models.CharField(max_length=50)),
                ('dimensiones', models.TextField()),
                ('habitat', models.TextField()),
                ('estado_conservacion', models.TextField()),
                ('importancia_ecologica', models.TextField()),
                ('como_reconocerlo', models.TextField()),
                ('imagen', models.URLField()),
                ('geom_wkt', django.contrib.gis.db.models.fields.MultiPolygonField(srid=25830)),
            ],
        ),
    ]
