from rest_framework import viewsets
from intersections.serializers import IntersectionSerializer
from intersections.models import Intersection


# Create your views here.
class IntersectionViewSet(viewsets.ModelViewSet):
    queryset = Intersection.objects.all()
    serializer_class = IntersectionSerializer

# Create your views here.
