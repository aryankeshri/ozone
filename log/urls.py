from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from .views import *

urlpatterns = [
    url(r'^$', adminleague, name='adminleague'),
    url(r'^team/$', adminteam, name='adminteam'),
    url(r'^news/$', adminnews, name='adminnews'),
    url(r'^photo-of-day/$', adminpod, name='adminpod'),
    url(r'^players/$', adminplayers, name='adminplayers'),
    url(r'^fixtures/$', adminfixtures, name='adminfixtures'),
    url(r'^standings/$', adminstandings, name='adminstandings'),
    url(r'^events/$', adminevents, name='adminevents'),
    url(r'^fctv/$', adminfctv, name='adminfctv'),
    url(r'^league/delete/(?P<id>\d+)/$', delete_league, name='delete_league'),
    url(r'^team/delete/(?P<id>\d+)/$', delete_team, name='delete_team'),
    url(r'^news/delete/(?P<id>\d+)/$', delete_news, name='delete_news'),
    url(r'^photo-of-day/delete/(?P<id>\d+)/$', delete_pod, name='delete_pod'),
    url(r'^player/delete/(?P<id>\d+)/$', delete_player, name='delete_player'),
    url(r'^fixtures/delete/(?P<id>\d+)/$', delete_fixtures, name='delete_fixtures'),
    url(r'^standings/delete/(?P<id>\d+)/$', delete_standings, name='delete_standings'),
    url(r'^event/delete/(?P<id>\d+)/$', delete_event, name='delete_event'),
    url(r'^fctv/delete/(?P<id>\d+)/$', delete_fctv, name='delete_fctv'),
    url(r'league/update/(?P<id>\d+)/$', edit_league, name='edit_league'),
    url(r'team/update/(?P<id>\d+)/$', edit_team, name='edit_team'),
    url(r'news/update/(?P<id>\d+)/$', edit_news, name='edit_news'),
    url(r'photo-of-day/update/(?P<id>\d+)/$', edit_pod, name='edit_pod'),
    url(r'player/update/(?P<id>\d+)/$', edit_player, name='edit_player'),
    url(r'fixtures/update/(?P<id>\d+)/$', edit_fixtures, name='edit_fixtures'),
    url(r'standings/update/(?P<id>\d+)/$', edit_standings, name='edit_standings'),
    url(r'event/update/(?P<id>\d+)/$', edit_events, name='edit_events'),
    url(r'fctv/update/(?P<id>\d+)/$', edit_fctv, name='edit_fctv'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)