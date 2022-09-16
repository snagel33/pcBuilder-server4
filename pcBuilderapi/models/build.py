from django.db import models
from pcBuilderapi.models.builder import Builder
from pcBuilderapi.models.part import Part


class Build(models.Model):
    title = models.CharField(max_length=50)
    builder = models.ForeignKey(Builder, on_delete=models.CASCADE)
    img = models.CharField(max_length=500)
    price = models.IntegerField()
    rating = models.IntegerField()
    parts = models.ManyToManyField(Part, related_name="BuildParts", null=True, blank=True)