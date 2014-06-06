# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

import facebook

from .forms import AgendarForm


class AgendarFormView(FormView):
    template_name = 'fbpage/agendar_form.html'
    form_class = AgendarForm
    success_url = reverse_lazy('fb:agendar')

    def form_valid(self, form):
        auth = self.request.user.social_auth.get(provider='facebook')
        token = auth.extra_data['access_token']

        graph = facebook.GraphAPI(token)

        profile = graph.get_object("me")

        print profile

        # graph.put_photo(open('/home/lido/Pictures/wallpaper-925934.jpg'), 'Post com a API do facebook')
        graph.put_object("me", "feed", message="I am writing on my wall!")


# user = facebook.get_user_from_cookie(self.request.cookies, key, secret)
# if user:
#     graph = facebook.GraphAPI(user["access_token"])
#     profile = graph.get_object("me")
#     friends = graph.get_connections("me", "friends")

        return super(AgendarFormView, self).form_valid(form)
