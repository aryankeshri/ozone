from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from news.models import News
from fixtures.models import Standings, Fixtures
from league.models import League, Player, Team, OzonefcTeam
from .models import Event, Join, Ofctv, PhotoDay
from .forms import JoinForm


def home(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    # for Home page
    ofctvs = Ofctv.objects.all().order_by('-created')[:5]
    pods = PhotoDay.objects.filter(status='publish').order_by('-id')[:2]
    leagues = League.objects.all().order_by('-created')
    standings = Standings.objects.all()
    newss = News.objects.filter(status='publish').order_by('-publish')[2:12]
    latest_news = News.objects.filter(status='publish').order_by('-publish')[:2]

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,
        #home
        'ofctvs': ofctvs,
        'pods': pods,
        'leagues': leagues,
        'standings': standings,
        'newss': newss,
        'latest_news': latest_news,

    }
    return render(request, 'home.html', context)


def event(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    events = Event.objects.all().order_by('-date')[:20]

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,

        'events': events,
    }
    return render(request, 'events.html', context)

def news(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    latest = News.objects.filter(status='publish').order_by('-publish')[:1]
    newss = News.objects.filter(status='publish').order_by('-publish')[1:10]
    standings = Standings.objects.all()
    league = League.objects.all().order_by('-created')[:5]
    most_read = News.objects.filter(status='publish').order_by('-publish')[:5]

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,

        'latest': latest,
        'newss': newss,
        'standings': standings,
        'league': league,
        'most_read': most_read,
    }
    return render(request, 'news.html', context)

def news_detail(request, id=None):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    newss = News.objects.filter(status='publish')[:10]
    instance = get_object_or_404(News, id=id)
    most_read = News.objects.filter(status='publish').order_by('-publish')[:5]
    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,

        'newss': newss,
        'instance': instance,
        'most_read': most_read,
    }
    return render(request, 'news_details.html', context)

def news_ofcd(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    latest = News.objects.filter(status='publish').order_by('-publish')[:1]
    newss = News.objects.filter(status='publish').order_by('-publish')[1:10]
    standings = Standings.objects.all()
    league = League.objects.all().order_by('-created')[:5]
    most_read = News.objects.filter(status='publish').order_by('-publish')[:5]

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,

        'latest': latest,
        'newss': newss,
        'standings': standings,
        'league': league,
        'most_read': most_read,
    }
    return render(request, 'news-ofcb.html', context)

def news_ozone_academy(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    latest = News.objects.filter(status='publish').order_by('-publish')[:1]
    newss = News.objects.filter(status='publish').order_by('-publish')[1:10]
    standings = Standings.objects.all()
    league = League.objects.all().order_by('-created')[:5]
    most_read = News.objects.filter(status='publish').order_by('-publish')[:5]

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,

        'latest': latest,
        'newss': newss,
        'standings': standings,
        'league': league,
        'most_read': most_read,
    }
    return render(request, 'news-ozone-academy.html', context)


def team(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    standings = Standings.objects.all()
    league = League.objects.all().order_by('-created')[:5]
    most_read = News.objects.all().order_by('-publish')[:5]
    teams = OzonefcTeam.objects.all()
    player_list = Player.objects.all()
    # players = Player.objects.all()
    id = OzonefcTeam.objects.filter(team_name='OFCB')
    # player_list = Player.objects.all()
    players = Player.objects.all().filter(team_name_id=id)
    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,

        'standings': standings,
        'league': league,
        'most_read': most_read,
        'players': players,
        'teams': teams,
        # 'player_list': player_list,
    }
    return render(request, 'team.html', context)


def team_super_division(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    standings = Standings.objects.all()
    league = League.objects.all().order_by('-created')[:5]
    most_read = News.objects.all().order_by('-publish')[:5]
    teams = OzonefcTeam.objects.all()
    id = OzonefcTeam.objects.filter(team_name='team-super-division')
    # player_list = Player.objects.all()
    players = Player.objects.all().filter(team_name_id=id)

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,

        'standings': standings,
        'league': league,
        'most_read': most_read,
        'players': players,
        'teams': teams,
        # 'player_list': player_list,
    }
    return render(request, 'team_super_division.html', context)

def team_u17(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    standings = Standings.objects.all()
    league = League.objects.all().order_by('-created')[:5]
    most_read = News.objects.all().order_by('-publish')[:5]
    teams = OzonefcTeam.objects.all()
    id = OzonefcTeam.objects.filter(team_name='team-u17')
    print(id)
    # player_list = Player.objects.all()
    players = Player.objects.all().filter(team_name_id=id)

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,

        'standings': standings,
        'league': league,
        'most_read': most_read,
        'players': players,
        'teams': teams,
        # 'player_list': player_list,
    }
    return render(request, 'team_u17.html', context)

def team_u15(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    standings = Standings.objects.all()
    league = League.objects.all().order_by('-created')[:5]
    most_read = News.objects.all().order_by('-publish')[:5]
    teams = OzonefcTeam.objects.all()
    id = OzonefcTeam.objects.filter(team_name='team-u15')
    # player_list = Player.objects.all()
    players = Player.objects.all().filter(team_name_id=id)

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,

        'standings': standings,
        'league': league,
        'most_read': most_read,
        'players': players,
        'teams': teams,
        # 'player_list': player_list,
    }
    return render(request, 'team_u15.html', context)


def player(request, id=None):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    instance = get_object_or_404(Player, id=id)
    team_mates = Player.objects.filter(team_name_id=instance.team_name_id)

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,

        'instance': instance,
        'team_mates': team_mates,
    }
    return render(request, 'player.html', context)


def grassroots_programs(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]

    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,
    }
    return render(request, 'grassroots-program.html', context)


def residential_academy(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]

    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('residential_academy')
        else:
            form = JoinForm()  # an unbound form

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,
    }
    return render(request, 'residential-academy.html', context)


def bangalore_academy(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]

    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('bangalore_academy')
        else:
            form = JoinForm()  # an unbound form

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,
    }
    return render(request, 'bangalore-academy.html',context)


def fixtures_results(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    months = ['January','February','March','April','May','June','July','August','September','October','November','December'][::-1]
    standings = Standings.objects.all().order_by('-pts')
    leagues = League.objects.all().order_by('-created')
    fixtures = Fixtures.objects.all().order_by('-date')
    most_read = News.objects.all().order_by('-publish')[:5]

    context={
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,

        'months': months,
        'standings': standings,
        'leagues': leagues,
        'fixtures': fixtures,
        'most_read': most_read,
    }
    return render(request, 'fixtures-results.html', context)


def oftv(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    videos = Ofctv.objects.all().order_by('-id')[:11]

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,

        'videos': videos,
    }
    return render(request, 'fctv.html', context)


def oftv_details(request, id=None):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    instance = get_object_or_404(Ofctv, id=id)
    videos = Ofctv.objects.all().order_by('-id')[:11]
    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,

        'instance': instance,
        'videos': videos,
    }
    return render(request, 'ofcb-inner.html', context)


def club(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,
    }
    return render(request, 'the-club.html', context)


def partners(request):
    # for header
    recent_results = Fixtures.objects.filter(result=True).order_by('-date')[:2]
    upcomming_matches = Fixtures.objects.filter(result=False).order_by('-date')[:2]
    upcomming_matches2 = Fixtures.objects.filter(result=False).order_by('-date')[2:4]
    header_ofctv = Ofctv.objects.all().order_by('-created')[:6]
    form = JoinForm()

    if request.method == 'POST':
        form = JoinForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grassroots_programs')
        else:
            form = JoinForm()  # an unbound form

    context = {
        'recent_results': recent_results,
        'form': form,
        'header_ofctv': header_ofctv,
        'upcomming_matches': upcomming_matches,
        'upcomming_matches2': upcomming_matches2,
    }
    return render(request, 'partners_page.html', context)

