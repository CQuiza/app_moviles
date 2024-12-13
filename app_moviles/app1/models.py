from django.db import models
from django.contrib.gis.db import models as gis_models
from datetime import datetime

# Create your models here.
charFieldDjango = gis_models.CharField(null=False, max_length= 50)
textFieldDjango = gis_models.TextField(null=False)

class Especies_app(gis_models.Model):
    gid = models.AutoField(primary_key=True)
    geom_wkb = gis_models.BinaryField(null=False)
    fid = gis_models.BigIntegerField(null=False)
    cuadricula = gis_models.CharField(null=False, max_length=50)
    grupo = gis_models.CharField(null=False, max_length=50)
    genero = gis_models.CharField(null=False, max_length=50)
    especie = gis_models.CharField(null=False, max_length=50)
    nombre_cientifico = gis_models.CharField(null=False, max_length=50)
    nombre_comun = gis_models.CharField(null=False, max_length=50)
    dimensiones = gis_models.TextField(null=False)
    habitat = gis_models.TextField(null=False)
    estado_conservacion = gis_models.TextField(null=False)
    importancia_ecologica = gis_models.TextField(null=False)
    como_reconocerlo = gis_models.TextField(null=False)
    imagen = gis_models.URLField(null=False)
    geom_wkt = gis_models.MultiPolygonField(null=False, srid=25830)

    def __str__(self):
        return f"{self.nombre_cientifico} ({self.nombre_comun})"

