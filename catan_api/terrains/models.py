from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Terrain(models.Model):
    id = models.AutoField(primary_key=True)
    resource = models.CharField(max_length=50) 
