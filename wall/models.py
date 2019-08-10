""" modeli """
from django.db import models

# Create your models here.

class Objava(models.Model):
    """ model za objavo na zidu """
    tekst = models.CharField(max_length=500)
    def __str__(self):
        return self.tekst

class IzbrisanaObjava(models.Model):
    """ model za izbrisano objavo """
    tekst = models.CharField(max_length=500)
    def __str__(self):
        return self.tekst
