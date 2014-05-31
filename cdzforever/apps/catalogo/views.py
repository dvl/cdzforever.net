# -*- coding: utf-8 -*-

from django.db.models import F
from django.views.generic import ListView, DetailView

from .models import Serie, Episodio


class SerieListView(ListView):
    model = Serie


class EpisodioListView(ListView):
    model = Episodio

    def get_queryset(self, **kwargs):
        qs = super(EpisodioListView, self).get_queryset(**kwargs)
        qs = qs.filter(serie=self.kwargs['pk'])

        return qs


class EpisodioDetailView(DetailView):
    model = Episodio

    def dispatch(self, request, *args, **kwargs):
        pk = self.kwargs[self.pk_url_kwarg]
        self.model.objects.filter(pk=pk).update(acessos=F('acessos') + 1)

        return super(EpisodioDetailView, self).dispatch(request, *args, **kwargs)
