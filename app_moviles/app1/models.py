# Importamos los modelos de Django y los modelos GIS
from django.db import models
from django.contrib.gis.db import models as gis_models
from datetime import datetime

# Creamos campos de texto y caracteres para su uso en los modelos
charFieldDjango = gis_models.CharField(null=False, max_length= 50)
textFieldDjango = gis_models.TextField(null=False)

# Definimos el modelo para las especies
class Especies_app(gis_models.Model):
    gid = models.AutoField(primary_key=True)  # ID único para cada especie
    geom_wkb = gis_models.BinaryField(null=False)  # Campo para datos geométricos en formato binario
    fid = gis_models.BigIntegerField(null=False)  # ID adicional para la especie
    cuadricula = gis_models.CharField(null=False, max_length=50)  # Identificador de cuadrícula
    grupo = gis_models.CharField(null=False, max_length=50)  # Grupo taxonómico
    genero = gis_models.CharField(null=False, max_length=50)  # Género de la especie
    especie = gis_models.CharField(null=False, max_length=50)  # Nombre de la especie
    nombre_cientifico = gis_models.CharField(null=False, max_length=50)  # Nombre científico
    nombre_comun = gis_models.CharField(null=False, max_length=50)  # Nombre común
    dimensiones = gis_models.TextField(null=False)  # Dimensiones de la especie
    habitat = gis_models.TextField(null=False)  # Hábitat natural
    estado_conservacion = gis_models.TextField(null=False)  # Estado de conservación
    importancia_ecologica = gis_models.TextField(null=False)  # Importancia ecológica
    como_reconocerlo = gis_models.TextField(null=False)  # Descripción de cómo reconocer la especie
    imagen = gis_models.URLField(null=False)  # URL de la imagen de la especie
    geom_wkt = gis_models.MultiPolygonField(null=False, srid=25830)  # Campo geométrico en formato WKT

    def __str__(self):
        return f"especie: {self.gid} {self.nombre_cientifico} ({self.nombre_comun})"  # Representación en cadena de la especie
    
# Definimos el modelo para los reportes
class Reporte_app(gis_models.Model):
    gid = models.AutoField(primary_key=True)  # ID único para cada reporte
    geom_wkb = gis_models.BinaryField(null=False)  # Campo para datos geométricos en formato binario
    asunto = models.CharField(max_length= 20, choices= [('avistamiento', 'avistamiento'), ('ayuda', 'ayuda')])  # Asunto del reporte
    reporte = models.TextField(null= False)  # Descripción del reporte
    imagen = models.ImageField(upload_to='fotos_reportes/', null= True)  # Imagen del reporte
    verificado = models.BooleanField(default= False)  # Estado de verificación del reporte
    fecha_reporte = models.DateTimeField(auto_now_add=True)  # Fecha de creación del reporte
    geom_wkt =gis_models.MultiPointField(null = False, srid= 25830)  # Campo geométrico en formato WKT
    especie_gid = models.ForeignKey(Especies_app, on_delete=models.CASCADE)  # Relación con el modelo Especies_app

    def __str__(self):
        return f"Reporte: {self.gid}, {self.asunto}"  # Representación en cadena del reporte

# Definimos el modelo para los usuarios
class Usuario_app(gis_models.Model):
    id = models.AutoField(primary_key=True)  # ID único para cada usuario
    nombre = gis_models.CharField(null=False, max_length=50)  # Nombre del usuario
    correo_electronico = models.EmailField(null=False)  # Correo electrónico del usuario

    def __str__(self):
        return f"Usuario: {self.id}, {self.nombre}, {self.correo_electronico}"  # Representación en cadena del usuario

# Definimos el modelo para la relación entre reportes y especies
class Reporte_especies_app(models.Model):
    id = models.AutoField(primary_key=True)  # ID único para cada relación
    especie = models.ForeignKey(Especies_app, on_delete=models.CASCADE)  # Relación con el modelo Especies_app
    reporte = models.ForeignKey(Reporte_app, on_delete=models.CASCADE)  # Relación con el modelo Reporte_app
    usuario = models.ForeignKey(Usuario_app, on_delete=models.CASCADE)  # Relación con el modelo Usuario_app

    def __str__(self):
        return f"Reporte especie: {self.id}, {self.especie}, {self.reporte}, {self.usuario}"  # Representación en cadena de la relación
