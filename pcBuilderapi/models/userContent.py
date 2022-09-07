from turtle import title
from django.db import models
from pcBuilderapi.models import Builder

class UserContent(models.Model):
    builder = models.ForeignKey(Builder, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)