# -*- coding: utf-8 -*-

from tempfile import mkstemp

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.core.signing import BadSignature, SignatureExpired
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView, RedirectView

from braces.views import LoginRequiredMixin

import facebook

from .forms import AgendarFormSet
from .jobs import enqueue_photo


class TokenRequestView(LoginRequiredMixin, TemplateView):
    template_name = 'fbpage/token_request.html'


class StoreTokenView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('fb:agendar')

    def get(self, request, *args, **kwargs):
        # Se for usar mesmo o redis quero guardar
        # isso lá e não em cookie
        user = facebook.get_user_from_cookie(
            self.request.COOKIES,
            settings.FACEBOOK_APP_ID,
            settings.FACEBOOK_API_SECRET
        )

        response = super(StoreTokenView, self).get(request, *args, **kwargs)
        response.set_signed_cookie('access_token', user['access_token'],
                                   max_age=7200, httponly=True)
                                   # segundo facebook o token dura 2 horas

        return response


class AgendarFormView(LoginRequiredMixin, FormView):
    template_name = 'fbpage/agendar_form.html'
    form_class = AgendarFormSet
    success_url = reverse_lazy('fb:agendar')

    def dispatch(self, request, *args, **kwargs):
        try:
            self.access_token = self.request.get_signed_cookie('access_token')
        except (KeyError, BadSignature, SignatureExpired):
            return redirect('fb:token')

        return super(AgendarFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        graph_account = facebook.GraphAPI(self.access_token)

        profile = graph_account.get_object("me/accounts")

        # Não estou muito certo sobre isso...
        for page in profile['data']:
            if page['name'] == 'CDZForever':
                page_token = page['access_token']
                continue

        graph_page = facebook.GraphAPI(page_token)

        for f in form:
            data = f.cleaned_data

            if data:
                tmpfile = mkstemp()[1]  # talvez isso de problema com o sistema de arquivos do heroku

                with open(tmpfile, 'w') as f:
                    for c in data['imagem'].chunks():
                        f.write(c)
                    f.close()

                del data['imagem']

                enqueue_photo.delay(graph_page, tmpfile, data)

        return super(AgendarFormView, self).form_valid(form)
