from django.db import models

# Create your models here.


class CharacterType(models.Model):
    vector = models.IntegerField()
    token = models.CharField(max_length=200)
    frequency = models.FloatField()

    def __str__(self):
        return self.title


class WordType(models.Model):
    vector = models.IntegerField()
    token = models.CharField(max_length=200)
    frequency = models.FloatField()

    def __str__(self):
        return self.title
