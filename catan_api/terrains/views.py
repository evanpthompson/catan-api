from rest_framework import viewsets
from terrains.serializers import TerrainSerializer
from terrains.models import Terrain


# Create your views here.
class TerrainViewSet(viewsets.ModelViewSet):
    queryset = Terrain.objects.all()
    serializer_class = TerrainSerializer
            
