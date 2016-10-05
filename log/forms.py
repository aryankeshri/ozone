from django import forms
from django.utils.translation import ugettext_lazy as _
from core.models import PhotoDay, Event, Ofctv
from league.models import Team, League, Player
from news.models import News
from fixtures.models import Fixtures, Standings
from functools import partial
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import FormActions, StrictButton

DateInput = partial(forms.DateInput, {'class': 'datepicker', 'autocomplete': 'off'})


# League Add Form
class LeagueAddForm(forms.ModelForm):

    class Meta:
        model = League
        fields = ['league_name', 'start_date', 'end_date']
        widgets = {
            'league_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'start_date': forms.DateInput(attrs={'class':'datepicker form-control', 'placeholder': 'Date', 'autocomplete': 'off', 'id': 'id_start_date'}),
            'end_date': forms.DateInput(attrs={'class':'datepicker form-control', 'placeholder': 'Date', 'autocomplete': 'off', 'id':'id_end_date'}),
        }


# Team Add Form
class TeamAddForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['team_name', 'team_short_name', 'team_logo', 'league_name']
        widgets = {
            'team_name': forms.TextInput(attrs={'class': 'form-control'}),
            'team_short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'team_logo': forms.ClearableFileInput(attrs={'class': 'upload'}),
            'league_name': forms.Select(attrs={'class': 'form-control'}),
        }


# Player Add Form
class PlayerAddForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ['team_name',
                  'player_name',
                  'player_position',
                  'jersy_number',
                  'dob',
                  'born_state',
                  'nationality',
                  'about_player',
                  'image_player'
                  ]

        widgets = {
            'team_name': forms.Select(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class':'datepicker form-control', 'placeholder': 'Date', 'autocomplete': 'off'}),
            'about_player': forms.Textarea(attrs={'placeholder': 'Content', 'rows': '3', 'class': 'form-control'}),
            'image_player': forms.ClearableFileInput(attrs={'class': 'upload'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'player_position': forms.Select(attrs={'class': 'form-control'}),
            'jersy_number': forms.TextInput(attrs={'class': 'form-control'}),
            'born_state': forms.TextInput(attrs={'class': 'form-control'}),
            'player_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


# News Add Form
class NewsAddForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'author', 'image_news', 'body', 'publish', 'status']

        widgets = {
            'publish': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'body': forms.Textarea(attrs={'placeholder': 'Content', 'rows': '3', 'class': 'form-box'}),
            'image_news': forms.ClearableFileInput(attrs={'class': 'upload'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

# photo of Day add Form
class PodAddForm(forms.ModelForm):

    class Meta:
        model = PhotoDay
        fields = ['image', 'title', 'status']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'upload'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title_pod'}),
            'status': forms.Select(attrs={'class': 'form-control', 'id': 'status_pod'}),
        }
        errors = {
            'image': _('This field is required'),
            'title': _('This field is required'),
        }

# Fixtures Add Form
class FixturesAddForm(forms.ModelForm):

    class Meta:
        model = Fixtures

        fields = ['league_name', 'date', 'team1', 'team2', 'score1', 'score2', 'result']

        widgets = {
            'league_name': forms.Select(attrs={'class': 'form-control fixture'}),
            'date':forms.DateInput(attrs={'class':'datepicker form-control', 'placeholder': 'Date', 'autocomplete': 'off'}),
            'team1': forms.Select(attrs={'class': 'form-control'}),
            'team2': forms.Select(attrs={'class': 'form-control'}),
            'score1': forms.TextInput(attrs={'class': 'form-control'}),
            'score2': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def clean_team2(self):
        """ check to see if passwords match. """
        team2 = self.cleaned_data['team2']
        if 'team1' in self.cleaned_data:
            team1 = self.cleaned_data['team1']
            if team1 == team2:
                raise forms.ValidationError("team1 and team2 not be same")
        return team2

# Stangings Add Form
class StandingsAddForm(forms.ModelForm):

    class Meta:
        model = Standings
        fields = ['league','team', 'pld', 'w', 'd', 'l', 'gf', 'ga', 'gd', 'pts']
        widgets = {
            'league': forms.Select(attrs={'class': 'form-control'}),
            'team': forms.Select(attrs={'class': 'form-control'}),
            'pld': forms.TextInput(attrs={'class': 'form-control'}),
            'w': forms.TextInput(attrs={'class': 'form-control'}),
            'd': forms.TextInput(attrs={'class': 'form-control'}),
            'l': forms.TextInput(attrs={'class': 'form-control'}),
            'gf': forms.TextInput(attrs={'class': 'form-control'}),
            'ga': forms.TextInput(attrs={'class': 'form-control'}),
            'gd': forms.TextInput(attrs={'class': 'form-control'}),
            'pts':forms.TextInput(attrs={'class': 'form-control'}),
        }


# Events Add Form
class EventsAddForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['image', 'title', 'date', 'body']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'upload', 'id': 'id_image_event'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class':'datepicker form-control', 'placeholder': 'Date', 'autocomplete': 'off'}),
            'body': forms.Textarea(attrs={'placeholder': 'Content', 'rows': '3', 'class': 'form-control form-box'}),
        }


class OctvAddForm(forms.ModelForm):
    class Meta:
        TYPE_CHOICES = (
            ('all', 'all',),
            ('i-league', 'i-league'),
            ('champions-league', 'champions-league'),
            ('interview', 'interview'),
            ('documentary', 'documentary'),
        )
        model = Ofctv
        fields = ['video', 'title', 'type']
        widgets = {
            'video': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL of video...'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title....'}),
            'type': forms.RadioSelect(choices=TYPE_CHOICES),
        }

