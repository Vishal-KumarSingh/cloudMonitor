from django.db import models

# Create your models here.

class BookMarks(models.Model):
     path = models.CharField(max_length=255)
     name = models.CharField(max_length=100)
     