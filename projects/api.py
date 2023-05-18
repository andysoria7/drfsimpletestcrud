from .models import Project # Importamos nuestro models.
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer # Importamos nuestro serializer.

class ProjectViewSet(viewsets.ModelViewSet): # Aqui decimos que consultas se van a poder hacer.
    queryset = Project.objects.all() # Consulta todos los datos de una tabla.
    permission_classes = [permissions.AllowAny] # Aplica los permisos, "AllowAny" nos permite que cualquier app cliente o cliente pueda solicitar datos del servidor.
    serializer_class = ProjectSerializer # A partir de que serializer va a utilizar estos datos, como lo va a convertir.
    