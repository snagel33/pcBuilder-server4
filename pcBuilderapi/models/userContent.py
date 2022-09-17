from django.db import models
from pcBuilderapi.models import Builder
from pcBuilderapi.models.tag import Tag

class UserContent(models.Model):
    builder = models.ForeignKey(Builder, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag, related_name="tags")