import json
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect,  get_object_or_404, render_to_response
from django.utils.translation import ugettext_lazy as _
# Create your views here.
from core.models import PhotoDay, Ofctv
from league.models import League, Player, Team, OzonefcTeam
from news.models import News
from fixtures.models import Fixtures, Standings
from .forms import *


@login_required(login_url='/login/')
def adminleague(request):
    leagues = League.objects.all().order_by('-created')
    teams = Team.objects.all()
    form = LeagueAddForm()

    if request.method == 'POST':
        form = LeagueAddForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, _("Successfully Created"))
            return HttpResponseRedirect('/admin/')
        else:
            form = LeagueAddForm()  # an unbound form

    teamform = TeamAddForm()

    if request.method == 'POST':
        teamform = TeamAddForm(request.POST or None, request.FILES or None)
        if teamform.is_valid():
            instance = teamform.save(commit=False)
            print(instance)
            instance.save()
            messages.success(request, _("Successfully Created"))
            return HttpResponseRedirect('/admin/')
        else:
            teamform = TeamAddForm() # an unbound form

    context = {
        'leagues': leagues,
        'teams': teams,
        'form': form,
        'teamform': teamform,
    }
    return render(request, 'adminleaguenew.html', context)


@login_required(login_url='/login/')
def edit_league(request, id = None):
    leagues = League.objects.all().order_by('-created')
    teams = Team.objects.all()
    instance = get_object_or_404(League, id=id)
    form = LeagueAddForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, _("Successfully Updated"))
        return HttpResponseRedirect('/admin/')
    context = {
        'leagues': leagues,
        'teams': teams,
        'form': form,
        }
    return render(request, "adminleaguenew.html", context)


@login_required(login_url='/login/')
def delete_league(request, id=None):
    u = get_object_or_404(League, pk=id).delete()
    messages.success(request, _("Successfully Deleted"))
    return HttpResponseRedirect('/admin/')

@login_required(login_url='/login/')
def edit_team(request, id=None):
    leagues = League.objects.all().order_by('-created')
    teams = Team.objects.all()
    instance = get_object_or_404(Team, id=id)
    teamform = TeamAddForm(request.POST or None, request.FILES or None, instance=instance)
    if teamform.is_valid():
        instance = teamform.save(commit=False)
        instance.save()
        messages.success(request, _("Successfully Updated"))
        return HttpResponseRedirect('/admin/')
    context = {
        'teamform': teamform,
        'leagues': leagues,
        'teams': teams,
        }
    return render(request, "adminleaguenew.html", context)


@login_required(login_url='/login/')
def delete_team(request, id=None):
    u = get_object_or_404(Team, pk=id).delete()
    messages.success(request, _("Successfully Deleted"))
    return HttpResponseRedirect('/admin/')

@login_required(login_url='/login/')
def adminteam(request):
    teams = Team.objects.all()
    teamform = TeamAddForm()

    if request.method == 'POST':
        teamform = TeamAddForm(request.POST or None, request.FILES or None)
        if teamform.is_valid():
            instance = teamform.save(commit=False)
            print(instance)
            instance.save()
            messages.success(request, _("Successfully Created"))
            return HttpResponseRedirect('/admin/team/')
        else:
            teamform = TeamAddForm() # an unbound form

    context = {
        'teamform': teamform,
        'teams': teams,
    }
    return render(request, 'adminteamnew.html', context)


@login_required(login_url='/login/')
def adminnews(request):
    news = News.objects.all().order_by('-publish')

    newsform = NewsAddForm()
    if request.method == 'POST':
        newsform = NewsAddForm(request.POST or None, request.FILES)
        if newsform.is_valid():
            instance = newsform.save(commit=False)
            instance.save()
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect('/admin/news/')
        else:
            newsform = NewsAddForm()

    context = {
        'news': news,
        'newsform': newsform,
    }
    return render(request, 'adminnewsnew.html', context)


@login_required(login_url='/login/')
def edit_news(request, id=None):
    news = News.objects.all()
    instance = get_object_or_404(News, id=id)
    newsform = NewsAddForm(request.POST or None, request.FILES or None, instance=instance)
    if newsform.is_valid():
        instance = newsform.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect('/admin/news/')
    context = {
        'newsform': newsform,
        'news': news,
        }
    return render(request, "adminnewsnew.html", context)


@login_required(login_url='/login/')
def delete_news(request, id=None):
    u = get_object_or_404(News, pk=id).delete()
    messages.success(request, "Successfully Deleted")
    return HttpResponseRedirect('/admin/news/')


@login_required(login_url='/login/')
def adminpod(request):
    pod = PhotoDay.objects.all().order_by('-id')
    podform = PodAddForm()
    if request.method == 'POST':
        podform = PodAddForm(request.POST or None, request.FILES or None)
        if podform.is_valid():
            instance = podform.save(commit=False)
            instance.save()
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect('/admin/photo-of-day/')
        else:
            podform = PodAddForm()

    context = {
        'pod': pod,
        'podform': podform
    }

    return render(request, 'adminpodnew.html', context)


@login_required(login_url='/login/')
def edit_pod(request, id=None):
    pod = PhotoDay.objects.all().order_by('-id')
    instance = get_object_or_404(PhotoDay, id=id)
    podform = PodAddForm(request.POST or None, request.FILES or None, instance=instance)
    if podform.is_valid():
        instance = podform.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect('/admin/photo-of-day/')
    context = {
        'pod': pod,
        'podform': podform,
        }
    return render(request, "adminpodnew.html", context)


@login_required(login_url='/login/')
def delete_pod(request, id=None):
    u = get_object_or_404(PhotoDay, pk=id).delete()
    messages.success(request, "Successfully Deleted")
    return HttpResponseRedirect('/admin/photo-of-day/')


@login_required(login_url='/login/')
def adminplayers(request):
    players = Player.objects.all()
    teams = OzonefcTeam.objects.all()
    playerform = PlayerAddForm()
    if request.method == 'POST':
        playerform = PlayerAddForm(request.POST or None, request.FILES or None)
        if playerform.is_valid():
            instance = playerform.save(commit=False)
            instance.save()
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect('/admin/players/')
        else:
            playerform = PlayerAddForm()

    context = {
        'players': players,
        'teams': teams,
        'playerform': playerform,
    }

    return render(request, 'adminplayersnew.html', context)


@login_required(login_url='/login/')
def edit_player(request, id=None):
    players = Player.objects.all()
    teams = OzonefcTeam.objects.all()
    instance = get_object_or_404(Player, id=id)
    playerform = PlayerAddForm(request.POST or None, request.FILES or None, instance=instance)
    if playerform.is_valid():
        instance = playerform.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect('/admin/players/')
    context = {
        'playerform': playerform,
        'players': players,
        'teams': teams,
        }
    return render(request, "adminplayersnew.html", context)


@login_required(login_url='/login/')
def delete_player(request, id=None):
    u = get_object_or_404(Player, pk=id).delete()
    messages.success(request, "Successfully Deleted")
    return HttpResponseRedirect('/admin/players/')


@login_required(login_url='/login/')
def adminfixtures(request):
    fixtures = Fixtures.objects.all()
    fixturesform = FixturesAddForm()
    if request.method == 'POST':
        fixturesform = FixturesAddForm(request.POST or None)
        if fixturesform.is_valid():
            instance = fixturesform.save(commit=False)
            instance.save()
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect('/admin/fixtures/')
        else:
            print(fixturesform.errors)
    else:
        fixturesform = FixturesAddForm()

    context = {
        'fixtures': fixtures,
        'fixturesform': fixturesform
    }

    return render(request, 'adminfixturesnew.html', context)


@login_required(login_url='/login/')
def edit_fixtures(request, id=None):
    fixtures = Fixtures.objects.all()
    instance = get_object_or_404(Fixtures, id=id)
    fixturesform = FixturesAddForm(request.POST or None, request.FILES or None, instance=instance)
    if fixturesform.is_valid():
        instance = fixturesform.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect('/admin/fixtures/')
    context = {
        'fixturesform': fixturesform,
        'fixtures': fixtures,
        }
    return render(request, "adminfixturesnew.html", context)


@login_required(login_url='/login/')
def delete_fixtures(request, id=None):
    u = get_object_or_404(Fixtures, pk=id).delete()
    messages.success(request, "Successfully Deleted")
    return HttpResponseRedirect('/admin/fixtures/')


@login_required(login_url='/login/')
def adminstandings(request):
    leagues = League.objects.all()
    standings = Standings.objects.all()
    standingsform = StandingsAddForm()
    if request.method == 'POST':
        standingsform = StandingsAddForm(request.POST or None)
        if standingsform.is_valid():
            instance = standingsform.save(commit=False)
            instance.save()
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect('/admin/standings/')
        else:
            standingsform = StandingsAddForm()

    context = {
        'leagues': leagues,
        'standings': standings,
        'standingsform': standingsform
    }

    return render(request, 'adminstandingsnew.html', context)
    # return render(request, 'adminstandings.html', context)


@login_required(login_url='/login/')
def edit_standings(request, id=None):
    leagues = League.objects.all()
    standings = Standings.objects.all()
    instance = get_object_or_404(Standings, id=id)
    standingsform = StandingsAddForm(request.POST or None, request.FILES or None, instance=instance)
    if standingsform.is_valid():
        instance = standingsform.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect('/admin/standings/')
    context = {
        'standingsform': standingsform,
        'leagues': leagues,
        'standings': standings,
        }
    return render(request, "adminstandingsnew.html", context)


@login_required(login_url='/login/')
def delete_standings(request, id=None):
    u = get_object_or_404(Standings, pk=id).delete()
    return HttpResponseRedirect('/admin/standings/')


@login_required(login_url='/login/')
def adminevents(request):
    events = Event.objects.all()
    eventform = EventsAddForm()
    if request.method == 'POST':
        eventform = EventsAddForm(request.POST or None, request.FILES or None)
        if eventform.is_valid():
            instance = eventform.save(commit=False)
            instance.save()
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect('/admin/events/')
        else:
            eventform = EventsAddForm()

    context = {
        'events': events,
        'eventform': eventform,
    }

    return render(request, 'admineventsnew.html', context)


@login_required(login_url='/login/')
def edit_events(request, id=None):
    events = Event.objects.all()
    instance = get_object_or_404(Event, id=id)
    eventform = EventsAddForm(request.POST or None, request.FILES or None, instance=instance)
    if eventform.is_valid():
        instance = eventform.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect('/admin/events/')
    context = {
        'eventform': eventform,
        'events': events,
        }
    return render(request, "admineventsnew.html", context)


@login_required(login_url='/login/')
def delete_event(request, id=None):
    u = get_object_or_404(Event, pk=id).delete()
    messages.success(request, "Successfully Deleted")
    return HttpResponseRedirect('/admin/events/')

# def get_team(request, league_id):
#     # league = League.objects.get(pk=league_id)
#     teams = Team.objects.filter(pk=league_id)
#     print(teams)
#     # json_models = serializers.serialize("json", models)
#     team_dict = {}
#     for t in teams:
#         print(t)
#         team_dict[t.id] = t.team_name
#         print(team_dict)
#     return HttpResponse(json.dumps(team_dict), mimetype="application/json")


# def all_json_models(request, league_id):
#     current_league = League.objects.get(id=league_id)
#     models = Team.objects.all().filter(league=current_league)
#     json_models = serializers.serialize("json", models)
#     return HttpResponse(json_models, mimetype="application/javascript")

@login_required(login_url='/login/')
def adminfctv(request):
    videos = Ofctv.objects.all().order_by('-created')

    fctvform = OctvAddForm()
    if request.method == 'POST':
        fctvform = OctvAddForm(request.POST or None)
        if fctvform.is_valid():
            instance = fctvform.save(commit=False)
            instance.save()
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect('/admin/fctv/')
        else:
            fctvform = OctvAddForm()

    context = {
        'videos': videos,
        'fctvform': fctvform,
    }
    return render(request, 'adminfctvnew.html', context)


@login_required(login_url='/login/')
def edit_fctv(request, id=None):
    videos = Ofctv.objects.all().order_by('-created')
    instance = get_object_or_404(Ofctv, id=id)
    fctvform = OctvAddForm(request.POST or None, instance=instance)
    if fctvform.is_valid():
        instance = fctvform.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect('/admin/fctv/')
    context = {
        'fctvform': fctvform,
        'videos': videos,
        }
    return render(request, "adminfctvnew.html", context)


@login_required(login_url='/login/')
def delete_fctv(request, id=None):
    u = get_object_or_404(Ofctv, pk=id).delete()
    messages.success(request, "Successfully Deleted")
    return HttpResponseRedirect('/admin/fctv/')


