from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^the-club/$', club, name='club'),
    url(r'^events/$', event, name='event'),
    url(r'^news/$', news, name='news'),
    url(r'^news/news-ofcd/$', news_ofcd, name='news_ofcd'),
    url(r'^news/news-ozone-academy/$', news_ozone_academy, name='news_ozone_academy'),
    url(r'^news/(?P<id>\d+)/$', news_detail, name='news_detail'),
    url(r'^team/$', team, name='team'),
    url(r'^team/team-super-division/$', team_super_division, name='team_super_division'),
    url(r'^team/team-u17/$', team_u17, name='team_u17'),
    url(r'^team/team-u15/$', team_u15, name='team_u15'),
    url(r'^grassroots-programs/$', grassroots_programs, name='grassroots_programs'),
    url(r'^grassroots-programs/residential-academy/$', residential_academy, name='residential_academy'),
    url(r'^grassroots-programs/bangalore-academy/$', bangalore_academy, name='bangalore_academy'),
    url(r'^player/(?P<id>\d+)/$', player, name='player'),
    url(r'^fixtures-results/$', fixtures_results, name='fixtures_results'),
    url(r'^ofcb/$', oftv, name='oftv'),
    url(r'^ofcb/ofcb-inner/(?P<id>\d+)/$', oftv_details, name='oftv_details'),
    url(r'^partners/$', partners, name='partners'),
]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)