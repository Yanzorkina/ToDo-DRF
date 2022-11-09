
from django.db import models

class Author(models.Model):
    username = models.CharField(max_length=64, unique=True)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.CharField(
        max_length=256,
        unique=True)
