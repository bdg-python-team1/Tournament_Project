from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime


class Tournament(models.Model):
    name = models.CharField(max_length=250)
    date_created = models.DateTimeField(default=datetime.now())
    player1 = models.CharField(max_length=150)
    player2 = models.CharField(max_length=150)
    player3 = models.CharField(max_length=150)
    player4 = models.CharField(max_length=150)
    player5 = models.CharField(max_length=150)
    player6 = models.CharField(max_length=150)
    player7 = models.CharField(max_length=150)
    player8 = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tournament, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player1 = models.CharField(max_length=150)
    player2 = models.CharField(max_length=150)
    score1 = models.PositiveIntegerField()
    score2 = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Matches'

    def __str__(self):
        return str(self.player1) + ' - ' + str(self.player2)