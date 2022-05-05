from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Note(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.PROTECT, null=True)
    text = models.TextField(verbose_name="Текст", null=True)
    image = models.ImageField(upload_to="upload_image/", null=True)