from rest_framework import serializers # para crear las clases
from rest_framework_gis.serializers import GeoFeatureModelSerializer
# from django.contrib.auth.models import User # para manejar usuarios con django
from .models import Especies_app # importar el modelo de la app1


# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     email = serializers.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

#     def create(self, validated_data):
#         user = User(
#             username=validated_data['username'],
#             email=validated_data['email']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user


# class OwnersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Owners
#         fields = '__all__'

# class MunicipalitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Municipality
#         fields = '__all__'

class EspeciesSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Especies_app
        
        geo_field = 'geom_wkt'
        id_field = False
        fields = ('gid', 'fid', 'cuadricula', 'grupo', 'genero', 'especie', 'nombre_cientifico', 'nombre_comun', 'dimensiones', 'habitat', 'estado_conservacion', 'importancia_ecologica', 'como_reconocerlo', 'imagen')

# # class DeptosSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Deptos
# #         fields = '__all__'

# # class MpiosSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Mpios
# #         fields = '__all__'

# class PartySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Party
#         fields = '__all__'