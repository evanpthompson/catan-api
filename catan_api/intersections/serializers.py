from intersections.models import Intersection
from rest_framework import serializers


class PathSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intersection
        fields = ('id')


