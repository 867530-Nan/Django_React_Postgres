from django.db import models

# Create your models here.


class CharacterTypes(models.Model):
    vector = models.IntegerField()
    token = models.CharField(max_length=200)
    frequency = models.FloatField()


class WordTypes(models.Model):
    vector = models.IntegerField()
    token = models.CharField(max_length=200)
    frequency = models.FloatField()
