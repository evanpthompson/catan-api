from __future__ import unicode_literals

from django.db import models
from intersections.models import Intersection
from paths.models import Path
from terrains.models import Terrain

# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True)

    @classmethod
    def create(cls):
        board = cls()
        board.save()
        for i in range(54):
            Intersection.objects.create(board_id=board.id)

        for i in range(70):
            Path.objects.create(board_id=board.id)

        for i in range(19):
            Terrain.objects.create(board_id=board.id)

        return board
