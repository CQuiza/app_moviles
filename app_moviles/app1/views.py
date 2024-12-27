# Importamos las funciones necesarias de Django y Django REST Framework
from django.shortcuts import render

from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.http import JsonResponse
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt

# Importamos los serializadores y modelos de nuestra aplicación
from .serializers import EspeciesSerializer, ReporteSerializer, UsuarioSerializer, ReporteEspecieSerializer
from .models import Especies_app, Reporte_app, Usuario_app, Reporte_especies_app

import json  # Importamos la biblioteca JSON para manejar datos en formato JSON

# Clase para manejar las vistas de Especies
class EspeciesViews(ReadOnlyModelViewSet):
    serializer_class = EspeciesSerializer  # Especificamos el serializador a usar
    queryset = Especies_app.objects.all()  # Consultamos todas las especies
    permission_classes = [AllowAny]  # Permitimos acceso a cualquier usuario

# Clase para manejar las vistas de Reportes
class ReporteViews(ReadOnlyModelViewSet):
    serializer_class = ReporteSerializer  # Especificamos el serializador a usar
    queryset = Reporte_app.objects.all()  # Consultamos todos los reportes
    permission_classes = [AllowAny]  # Permitimos acceso a cualquier usuario

# Clase para manejar las vistas de Usuarios
class UsuarioViews(ReadOnlyModelViewSet):
    serializer_class = UsuarioSerializer  # Especificamos el serializador a usar
    queryset = Usuario_app.objects.all()  # Consultamos todos los usuarios
    permission_classes = [AllowAny]  # Permitimos acceso a cualquier usuario

# Clase para manejar las vistas de Reportes de Especies
class ReporteEspeciesViews(ReadOnlyModelViewSet):
    serializer_class = ReporteEspecieSerializer  # Especificamos el serializador a usar
    queryset = Reporte_especies_app.objects.all()  # Consultamos todas las relaciones entre reportes y especies
    permission_classes = [AllowAny]  # Permitimos acceso a cualquier usuario

# Decorador para permitir solicitudes sin protección CSRF
@csrf_exempt
def create_reporte_especie(request):
    # Verificamos si la solicitud es de tipo POST
    if request.method == "POST":
        try:
            # Cargamos los datos del cuerpo de la solicitud
            data = json.loads(request.body)

            # Extracción de datos del cuerpo de la solicitud
            especie_id = data.get("especie_id")  # ID fijo de Especie
            reporte_asunto = data.get("reporte_asunto")  # Asunto del reporte
            reporte_geom = data.get("reporte_geom")  # Geometría del reporte
            reporte_imagen = data.get("reporte_imagen")  # URL de la imagen del Reporte
            reporte_descripcion = data.get("reporte_descripcion")  # Descripción del Reporte
            usuario_nombre = data.get("usuario_nombre")  # Nombre del Usuario
            usuario_correo = data.get("usuario_correo")  # Correo del Usuario

            # Validación básica de datos
            if not (especie_id and reporte_asunto and reporte_descripcion and reporte_geom and usuario_nombre and usuario_correo):
                return JsonResponse({"error": "Faltan datos obligatorios"}, status=400)  # Retornamos error si faltan datos

            # Comenzar la transacción atómica
            with transaction.atomic():
                # Verificar que la especie existe
                especie = Especies_app.objects.get(gid=especie_id)  # Buscamos la especie por su ID

                # Crear el reporte
                reporte = Reporte_app.objects.create(asunto=reporte_asunto,
                                                     reporte=reporte_descripcion,
                                                     imagen=reporte_imagen,
                                                     geom_wkt=reporte_geom,
                                                     especie_gid=especie)  # Creamos el reporte

                # Verificar si el usuario existe
                usuario, creado = Usuario_app.objects.get_or_create(
                    correo_electronico=usuario_correo,
                    defaults={"nombre": usuario_nombre}  # Creamos el usuario si no existe
                )

                # Crear la entrada en la tabla pivote
                reporte_especie = Reporte_especies_app.objects.create(
                    especie=especie,
                    reporte=reporte,
                    usuario=usuario  # Creamos la relación entre el reporte, la especie y el usuario
                )

            # Respuesta exitosa
            return JsonResponse({
                "message": "ReporteEspecie creado con éxito"  # Mensaje de éxito
            }, status=201)

        except Especies_app.DoesNotExist:
            return JsonResponse({"error": "Especie no encontrada"}, status=404)  # Error si la especie no existe
        except Exception as e:
            return JsonResponse({"error": [str(e), 'estatus:500']}, status=500)  # Error genérico

    return JsonResponse({"error": "Método HTTP no permitido"}, status=405)  # Error si el método no es permitido

# Decorador para permitir solicitudes sin protección CSRF
@csrf_exempt
def list_reporte_especie(request):
    # Verificamos si la solicitud es de tipo GET
    if request.method == "GET":
        try:
            # Consultamos los reportes de especies y sus relaciones
            pivote_data = Reporte_especies_app.objects.select_related('especie', 'reporte', 'usuario').all()
            results = [
                {   "id": pivote.id,  # ID de la relación
                    "especie": {
                        "gid": pivote.especie.gid,  # ID de la especie
                        "nombre_cientifico": pivote.especie.nombre_cientifico,  # Nombre científico de la especie
                        "nombre_comun": pivote.especie.nombre_comun  # Nombre común de la especie
                    },
                    "reporte": {
                        "gid": pivote.reporte.gid,  # ID del reporte
                        "asunto": pivote.reporte.asunto,  # Asunto del reporte
                        "descripcion": pivote.reporte.reporte,  # Descripción del reporte
                        # "imagen": pivote.reporte.imagen,  # Imagen del reporte (comentado)
                        "geom_wkt": str(pivote.reporte.geom_wkt),  # Geometría del reporte
                        "fecha_reporte": str(pivote.reporte.fecha_reporte)  # Fecha del reporte
                    },
                    "usuario": {
                        "id": pivote.usuario.id,  # ID del usuario
                        "nombre": pivote.usuario.nombre,  # Nombre del usuario
                        "correo": pivote.usuario.correo_electronico  # Correo del usuario
                    }
                }
                for pivote in pivote_data  # Iteramos sobre los datos obtenidos
            ]
            return JsonResponse({"Data": results}, safe=False)  # Retornamos los resultados en formato JSON
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)  # Error genérico
            
    return JsonResponse({"error": "Método HTTP no permitido"}, status=405)  # Error si el método no es permitido