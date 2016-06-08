from paths.models import Path
from rest_framework import serializers


class PathSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Path
        fields = ('id')



