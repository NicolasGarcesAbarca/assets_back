from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=30)
    rut = models.CharField(max_length=30)
