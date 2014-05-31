from django.conf.urls import patterns, url

from .views import SerieListView, EpisodioListView, EpisodioDetailView

urlpatterns = patterns(
    '',

    url(r'^series/$', SerieListView.as_view(), name='series'),
    url(r'^episodios/(?P<pk>.*)/$', EpisodioListView.as_view(), name='episodios'),
    url(r'^download/(?P<pk>.*)/$', EpisodioDetailView.as_view(), name='download'),
)
