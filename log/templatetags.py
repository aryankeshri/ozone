from django import template
from league.models import *


register = template.Library()



@register.inclusion_tag("adminstandings.html")

def league_select():
    league_list = League.objects.all()
    return {'league_list' : league_list}