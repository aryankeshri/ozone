from django.contrib import admin

# Register your models here.

from .models import Team, Player, League, OzonefcTeam


class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'team_short_name', 'logo', 'league_name']
    list_per_page = 10
    list_editable = ['league_name']

    class Meta:
        model=Team

class LeagueAdmin(admin.ModelAdmin):
    list_display = ['league_name', 'start_date', 'end_date']
    list_per_page = 10

    class Meta:
        model = League


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'player_position', 'jersy_number', 'dob', 'born_state', 'nationality', 'about_player', 'pic']
    list_per_page = 10
    search_fields = ['player_name']

    class Meta:
        model = Player

class OzonefcTeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'team_short_name', 'logo']

    class Meta:
        model = OzonefcTeam




admin.site.register(League, LeagueAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(OzonefcTeam, OzonefcTeamAdmin)
