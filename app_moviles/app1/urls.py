"""
Configuración de URL para el proyecto dj_project_1.

La lista `urlpatterns` dirige las URLs a las vistas. Para más información, por favor consulta:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Ejemplos:
Vistas de función
    1. Agrega una importación:  from my_app import views
    2. Agrega una URL a urlpatterns:  path('', views.home, name='home')
Vistas basadas en clases
    1. Agrega una importación:  from other_app.views import Home
    2. Agrega una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluyendo otro archivo de configuración de URL
    1. Importa la función include() desde django.urls: from django.urls import include, path
    2. Agrega una URL a urlpatterns: path('blog/', include('blog.urls'))
"""
# from django.contrib import admin  # Importación del módulo de administración de Django
from django.urls import path, re_path, include  # Importamos las funciones necesarias para definir las rutas
from app1 import views  # Importamos las vistas de la aplicación app1
from rest_framework import routers  # Importamos los routers de Django REST Framework
from rest_framework.documentation import include_docs_urls  # Importamos la función para incluir documentación de la API

from django.conf import settings  # Importamos la configuración del proyecto
from django.conf.urls.static import static  # Importamos la función para servir archivos estáticos

# Definimos routers para las diferentes aplicaciones
router_especies = routers.DefaultRouter()  # Router para las especies
router_reportes = routers.DefaultRouter()  # Router para los reportes
router_usuarios = routers.DefaultRouter()  # Router para los usuarios
router_reportes_especies = routers.DefaultRouter()  # Router para los reportes de especies

# Personalización de routers
router_especies.register(r'', views.EspeciesViews, 'EspeciesApp')  # Registramos las vistas de especies
router_reportes.register(r'', views.ReporteViews, 'ReporteApp')  # Registramos las vistas de reportes
router_usuarios.register(r'', views.UsuarioViews, 'UsuarioApp')  # Registramos las vistas de usuarios
router_reportes_especies.register(r'', views.ReporteEspeciesViews)  # Registramos las vistas de reportes de especies

# Generamos los endpoints para todas las consultas
urlpatterns = [
    
    re_path('create_reporte_especie/', views.create_reporte_especie),  # Ruta para crear un reporte de especie
    re_path('list_reporte_especie/', views.list_reporte_especie),  # Ruta para listar reportes de especies

    path('especies_app/', include(router_especies.urls)),  # Ruta para la aplicación de especies
    path('reportes_app/', include(router_reportes.urls)),  # Ruta para la aplicación de reportes
    path('usuarios_app/', include(router_usuarios.urls)),  # Ruta para la aplicación de usuarios
    path('reportes_especies_app/', include(router_reportes_especies.urls)),  # Ruta para la aplicación de reportes de especies

    # Documentación de la API
    path('docs/', include_docs_urls(title='Documentación de la API')),  # Ruta para la documentación de la API
]

# Configuración para servir archivos de medios en desarrollo
if settings.DEBUG:  # Verificamos si estamos en modo de depuración
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Servimos archivos de medios
