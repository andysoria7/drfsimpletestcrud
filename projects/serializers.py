from rest_framework import serializers # Importamos desde nuestro modulo rest_framework.
from .models import Project # Importamos nuestro modelo para decir que esta basado en el mismo.

class ProjectSerializer(serializers.ModelSerializer): # Esto va a convertir un modelo en datos que podran ser consultados.
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at') # agregamos los campos que tiene models.
        read_only_fields = ('created_at',) # Campos de solo lectura.