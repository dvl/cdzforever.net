from django.conf.urls import patterns, url

from .views import SerieListView, EpisodioListView, EpisodioDetailView, ReporteFormView

urlpatterns = patterns(
    '',

    url(r'^series/$', SerieListView.as_view(), name='series'),
    url(r'^episodios/(?P<pk>.*)/$', EpisodioListView.as_view(), name='episodios'),
    url(r'^download/(?P<pk>.*)/$', EpisodioDetailView.as_view(), name='download'),
    url(r'^reporte/(?P<pk>.*)/$', ReporteFormView.as_view(), name='reporte'),
)
