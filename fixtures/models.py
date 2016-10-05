from django.db import models

# Create your models here.
from league.models import League, Team

class Fixtures(models.Model):
    league_name = models.ForeignKey(League, unique=False, blank=False, null=False, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, related_name='team1',  unique=False, blank=False, null=False)
    team2 = models.ForeignKey(Team, related_name='team2',  unique=False, blank=False, null=False)
    score1 = models.CharField(max_length=2, blank=True, default=None)
    score2 = models.CharField(max_length=2, blank=True, default=None)
    date = models.DateField()
    result = models.BooleanField(default='0')

    class Meta:
        unique_together = ('league_name', "team1", "team2",)

    def __str__(self):
        return str(self.league_name)

class Standings(models.Model):
    league = models.ForeignKey(League, blank=False, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False, null=False)
    pld = models.IntegerField(blank=False, null=False)
    w = models.IntegerField(blank=True, null=False)
    d = models.IntegerField(blank=True, null=False)
    l = models.IntegerField(blank=True, null=False)
    gf = models.IntegerField(blank=True, null=False)
    ga = models.FloatField(max_length=4, blank=False, null=False)
    gd = models.FloatField(max_length=4, blank=False, null=False)
    pts = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.league)
