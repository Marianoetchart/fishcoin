from django.db import models

# Create your models here.


class Fish(models.Model):
        code = models.CharField(max_length=255)
        created = models.DateTimeField('auto_now_add=True')
        weight = models.CharField(max_length=255)
        type = models.CharField(max_length=255)
        species = models.CharField(max_length=255)
        latitude  = models.FloatField()
        longitude = models.FloatField()
        photo = models.URLField(max_length=200)











