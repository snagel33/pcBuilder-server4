from turtle import title
from django.db import models
from pcBuilderapi.models import Builder


class Build(models.Model):
    title = models.CharField(max_length=50)
    builder = models.ForeignKey(Builder, on_delete=models.CASCADE)
    img = models.CharField(max_length=500)
    price = models.IntegerField()
    rating = models.IntegerField()