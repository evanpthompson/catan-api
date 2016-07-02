from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Intersection(models.Model):
    id = models.AutoField(primary_key=True)
    board = models.ForeignKey('boards.Board', on_delete=models.CASCADE)
