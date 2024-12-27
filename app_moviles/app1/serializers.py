from rest_framework import serializers  # Importamos el módulo serializers para crear las clases de serialización
from rest_framework_gis.serializers import GeoFeatureModelSerializer  # Importamos el serializador para manejar datos geoespaciales
# from django.contrib.auth.models import User  # Importamos el modelo User para manejar usuarios con Django
from .models import Especies_app, Reporte_app, Usuario_app, Reporte_especies_app  # Importamos los modelos de la aplicación app1

class EspeciesSerializer(GeoFeatureModelSerializer):  # Serializador para el modelo Especies_app
    class Meta:
        model = Especies_app  # Especificamos el modelo a usar
        
        geo_field = 'geom_wkt'  # Campo geoespacial a utilizar
        id_field = False  # No incluir el campo ID
        fields = ('gid', 'fid', 'cuadricula', 'grupo', 'genero', 'especie', 'nombre_cientifico', 'nombre_comun', 'dimensiones', 'habitat', 'estado_conservacion', 'importancia_ecologica', 'como_reconocerlo', 'imagen')  # Campos a incluir en el serializador

class ReporteSerializer(GeoFeatureModelSerializer):  # Serializador para el modelo Reporte_app

    class Meta:
        model = Reporte_app  # Especificamos el modelo a usar

        geo_field = 'geom_wkt'  # Campo geoespacial a utilizar
        id_field = False  # No incluir el campo ID
        fields = ('gid', 'asunto', 'reporte', 'imagen', 'verificado', 'especie_gid')  # Campos a incluir en el serializador

class UsuarioSerializer(serializers.ModelSerializer):  # Serializador para el modelo Usuario_app

    class Meta:
        model = Usuario_app  # Especificamos el modelo a usar
        fields = ('id', 'nombre', 'correo_electronico')  # Campos a incluir en el serializador

class ReporteEspecieSerializer(serializers.ModelSerializer):  # Serializador para el modelo Reporte_especies_app

    class Meta:
        model = Reporte_especies_app  # Especificamos el modelo a usar
        fields = ('id', 'especie', 'reporte', 'usuario')  # Campos a incluir en el serializador
