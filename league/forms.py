from django import forms
from django.db import models
from .models import Team, League, Player


# Team Add Form
class TeamAddForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'team_short_name', 'team_logo']
        widgets = {
            'team_name': forms.TextInput(attrs={'placeholder': u'Type team name'}),
            'team_short_name': forms.TextInput(attrs={'placeholder': u'Type Short name of team'}),
        }


# League Add Form
class LeagueAddForm(forms.ModelForm):
    # teams = forms.ModelMultipleChoiceField(queryset=Team.objects.all(), required=False,
    #                                        widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = League
        fields = ['league_name', 'start_date', 'end_date', 'teams']
        widgets = {
            'league_name': forms.TextInput(attrs={'placeholder': u'Type league name'}),
            'start_date': forms.DateInput(),
            'end_date': forms.DateInput(),
        }



# Player Add Form
class PlayerAddForm(forms.ModelForm):
    team_name = status = forms.ModelChoiceField(label="Team", queryset=Team.objects.all(),
                                                widget=forms.Select(attrs={'class':'selector'}))
    class Meta:
        model = Player
        fields = ['player_name', 'player_position', 'jersy_number', 'dob', 'born_state', 'nationality', 'about_player', 'image_player']
        widgets = {
            'player_name': forms.TextInput(attrs={'placeholder': u'Type player name'}),
            'jersy_number': forms.TextInput(attrs={'placeholder': u'Type player jersy number'}),
            'dob': forms.DateInput(),
            'born_state': forms.TextInput(attrs={'placeholder': u'Type player born state'}),
            'nationality': forms.TextInput(attrs={'placeholder': u'Type player nationality'}),
            'about_player': forms.Textarea(attrs={'placeholder': u'Type About some thing of player'}),
        }









