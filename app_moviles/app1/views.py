from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import EspeciesSerializer
from .models import Especies_app

class EspeciesViews(ReadOnlyModelViewSet):
    serializer_class = EspeciesSerializer
    queryset = Especies_app.objects.all()
    permission_classes = [AllowAny]