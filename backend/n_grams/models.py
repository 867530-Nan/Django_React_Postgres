from django.db import models


class CharacterType(models.Model):
    vector = models.IntegerField()
    token = models.CharField(max_length=200)
    frequency = models.FloatField()

    def __str__(self):
        return self.token


class WordType(models.Model):
    vector = models.IntegerField()
    token = models.CharField(max_length=200)
    frequency = models.FloatField()

    def __str__(self):
        return self.token
