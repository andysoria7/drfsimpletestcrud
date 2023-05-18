from rest_framework import routers # Modulo especial que creara todas las rutas basicas.
from .api import ProjectViewSet # Importamos ProjectViewset para que el router este basado en viewset.

router = routers.DefaultRouter() # Es el que va a crear el crud.

router.register('api/projects', ProjectViewSet, 'projects') # Registramos el nombre de la ruta "ruta", "la clase" y "name" (get, post, delete, put).

urlpatterns = router.urls # El va a generar las urls 





