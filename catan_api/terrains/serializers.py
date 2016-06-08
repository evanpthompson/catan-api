from terrains.models import Terrain
from rest_framework import serializers


class TerrainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Terrain
        fields = ('id', 'resource')




