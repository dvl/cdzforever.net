from django.conf.urls import patterns, url

from .views import SerieListView, EpisodioListView

urlpatterns = patterns(
    '',

    url(r'^series/$', SerieListView.as_view(), name='series'),
    url(r'^episodios/$', EpisodioListView.as_view(), name='epidosios'),
)
