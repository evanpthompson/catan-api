from django.test import TestCase
from boards.models import Board
from intersections.models import Intersection
from paths.models import Path
from terrains.models import Terrain

# Create your tests here.
class BoardTestCase(TestCase):
    def test_book_create(self):
        board_count = Board.objects.count()
        intersection_count = Intersection.objects.count()
        path_count = Path.objects.count()
        terrain_count = Terrain.objects.count()

        board = Board.create()
        print board
        board.save()

        self.assertEquals(board_count + 1, Board.objects.count())
        self.assertEquals(intersection_count + 54, Intersection.objects.count())
        self.assertEquals(path_count + 70, Path.objects.count())
        self.assertEquals(terrain_count + 19, Terrain.objects.count())

