# -*- coding: utf-8 -*-

from django.views.generic import View

from braces.views import JSONResponseMixin

from .models import Serie, Episodio


class _JSONResponseMixin(JSONResponseMixin):
    def get(self, request, *args, **kwargs):
        # Por mais que pareça que o Django retorna uma
        # lista de objetos ele na verdade retorna um unico
        # objeto do tipo ValuesQuerySet.
        qs = list(self.queryset)

        return self.render_json_response(qs)


class SerieListView(_JSONResponseMixin, View):
    queryset = Serie.objects.values('pk', 'nome')


class EpisodioListView(_JSONResponseMixin, View):
    queryset = Episodio.objects.values()
