from django.contrib import admin

# Register your models here.

from .models import Fixtures, Standings

class FixturesAdmin(admin.ModelAdmin):
    list_display = ['league_name', 'team1', 'team2', 'score1', 'score2', 'date', 'result']

    class Meta:
        model = Fixtures

class StandingsAdmin(admin.ModelAdmin):
    list_display = ['team', 'w', 'd', 'l', 'gf', 'ga', 'gd', 'pts']
    list_filter = ['league']
    class Meta:
        model = Standings


admin.site.register(Fixtures, FixturesAdmin)
admin.site.register(Standings, StandingsAdmin)

