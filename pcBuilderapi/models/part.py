from django.db import models
from pcBuilderapi.models.partType import PartType

class Part(models.Model):
    partType = models.ForeignKey(PartType, on_delete=models.CASCADE)
    maker = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    price = models.IntegerField()