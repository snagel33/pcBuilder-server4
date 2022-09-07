from django.db import models
from django.contrib.auth.models import User

class Builder(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userName = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    img = models.CharField(max_length=500)
    