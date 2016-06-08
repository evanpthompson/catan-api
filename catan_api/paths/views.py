from rest_framework import viewsets
from paths.serializers import PathSerializer
from paths.models import Path


# Create your views here.
class TerrainViewSet(viewsets.ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer
            

