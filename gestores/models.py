from django.db import models

class Gestor(models.Model):
    name = models.CharField(max_length=30)

