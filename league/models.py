from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

# League Model
class League(models.Model):
    league_name = models.CharField(verbose_name='League name', max_length=100, blank=False)
    start_date = models.DateField(verbose_name='Starting Date', blank=False)
    end_date = models.DateField(verbose_name='Ending Date', blank=False)
    created = models.DateTimeField(auto_now=True, null=True)
    # teams = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Teams', blank=False)


    def __str__(self):
        return str(self.league_name)


# Team model
class Team(models.Model):
    team_name = models.CharField(verbose_name='Enter the Team name', max_length=150, blank=False)
    team_short_name = models.CharField(verbose_name='Enter the short name', max_length=50, blank=False)
    team_logo = models.ImageField(upload_to='images/team_logo', verbose_name='logo', blank=False)
    league_name = models.ForeignKey(League, on_delete=models.CASCADE, related_name='league', default=None, blank=False)

    def __str__(self):
        return self.team_name

    def logo(self):
        return "<img src='{}' width=30px>" .format(self.team_logo.url)
    logo.allow_tags=True


# ozonefc Team
class OzonefcTeam(models.Model):
    team_name = models.CharField(verbose_name='Enter the Team name', max_length=150, blank=False)
    team_short_name = models.CharField(verbose_name='Enter the short name', max_length=50, blank=False)
    team_logo = models.ImageField(upload_to='images/team_logo', verbose_name='logo', blank=False)

    def __str__(self):
        return self.team_name

    def logo(self):
        return "<img src='{}' width=30px>" .format(self.team_logo.url)
    logo.allow_tags=True


# Player model
class Player(models.Model):

    POSITION_CHOICES = (
        ('goalkeeper', 'Goalkeeper'),
        ('defender', 'Defender'),
        ('midfielder', 'Midfielder'),
        ('forward', 'Forward'),
        ('allrounder', 'Allrounder'),
        ('--------', '--------'),
    )

    team_name = models.ForeignKey(OzonefcTeam, on_delete=models.CASCADE, verbose_name='OzoneFC Team name')
    player_name = models.CharField(verbose_name='Player name', max_length=100, blank= False)
    player_position = models.CharField(verbose_name='Playing position', choices=POSITION_CHOICES, default='--------', max_length=50, blank=False)
    jersy_number = models.CharField(verbose_name='Jersy number', max_length=3,  blank=False)
    dob = models.DateField(verbose_name='DOB', blank=False)
    born_state = models.CharField(verbose_name='Born state', max_length=100, blank=False)
    nationality = models.CharField(verbose_name='Nationality', max_length=50, blank=False)
    about_player = models.TextField(verbose_name='About player', blank=False)
    image_player = models.ImageField(upload_to='images/image-player', verbose_name='Image', blank=False)


    def __str__(self):
        return self.player_name

    def pic(self):
        return "<img src='{}' width=50px>" .format(self.image_player.url)
    pic.allow_tags=True

