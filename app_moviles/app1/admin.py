from django.contrib.gis import admin  # Importamos el módulo de administración GIS de Django
from .models import Especies_app, Reporte_app, Usuario_app, Reporte_especies_app  # Importamos los modelos de nuestra aplicación

# Clase personalizada para la administración de modelos GIS
class CustomGeoadmin(admin.GISModelAdmin):
    gis_widget_kwargs = {  # Configuración de los widgets GIS
        'attrs':{
            'default_zoom': 8,  # Zoom predeterminado del mapa
            'map_width': '100%',  # Ancho del mapa
            'map_height': '400px',  # Altura del mapa
            'show_form': False,  # Ocultar el formulario
            'default_lon': -0.34601042439420265,  # Longitud predeterminada
            'default_lat': 39.48243147884478,  # Latitud predeterminada
            'default_crs': 'EPSG:25830',  # Sistema de referencia de coordenadas predeterminado
        }
    }

@admin.register(Especies_app)  # Registramos el modelo Especies_app en el admin
class EspeciesAdmin(CustomGeoadmin):  # Clase de administración para Especies
    list_display = ('gid', 'nombre_cientifico', 'nombre_comun')  # Campos a mostrar en la lista

@admin.register(Reporte_app)  # Registramos el modelo Reporte_app en el admin
class ReportesAdmin(CustomGeoadmin):  # Clase de administración para Reportes
    list_display = ('gid', 'asunto', 'fecha_reporte', 'especie_gid')  # Campos a mostrar en la lista

@admin.register(Usuario_app)  # Registramos el modelo Usuario_app en el admin
class UsuariosAdmin(admin.ModelAdmin):  # Clase de administración para Usuarios
    list_display = ('id', 'nombre', 'correo_electronico')  # Campos a mostrar en la lista

@admin.register(Reporte_especies_app)  # Registramos el modelo Reporte_especies_app en el admin
class ReportesEspeciesAdmin(admin.ModelAdmin):  # Clase de administración para Reportes de Especies
    list_display = ('id', 'especie_id', 'reporte_id', 'usuario_id')  # Campos a mostrar en la lista