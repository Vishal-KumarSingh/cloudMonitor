from django.db import models

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=255)
    softwarename = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    installcmd = models.CharField(max_length=255 , default='')
    
class Sripts(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    script = models.TextField()