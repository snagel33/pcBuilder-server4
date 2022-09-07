from django.db import models
from pcBuilderapi.models.build import Build
from pcBuilderapi.models.part import Part

class BuildPart(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    build = models.ForeignKey(Build, on_delete=models.CASCADE)