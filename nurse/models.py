from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Hospital(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to="hospital")

    