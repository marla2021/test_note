from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Note(models.Model):
    text = models.CharField(max_length=30)