# -*- coding: utf-8 -*-

from django.views.generic import ListView

from .models import Serie, Episodio


class SerieListView(ListView):
    model = Serie


class EpisodioListView(ListView):
    model = Episodio

    def get_queryset(self, **kwargs):
        qs = super(EpisodioListView, self).get_queryset(**kwargs)
        qs = qs.filter(serie=self.kwargs['pk'])

        return qs
