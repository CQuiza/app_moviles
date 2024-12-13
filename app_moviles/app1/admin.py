from django.contrib.gis import admin
from .models import Especies_app #, PropertyBounding


class CustomGeoadmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        'attrs':{
            'default_zoom': 8,
            'map_width': '100%',
            'map_height': '400px',
            'show_form': False,
            'default_lon': -0.34601042439420265,
            'default_lat': 39.48243147884478, 
            'default_crs': 'EPSG:25830',
            
        }
    }

@admin.register(Especies_app)
class OwnersAdmin(CustomGeoadmin):
    list_display = ('gid', 'nombre_cientifico', 'nombre_comun')