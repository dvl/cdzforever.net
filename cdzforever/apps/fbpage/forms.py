# -*- coding: utf-8 -*-

from django import forms


class AgendarForm(forms.Form):
    texto = forms.CharField(required=False)
    datahora = forms.DateTimeField(required=False)
    imagem = forms.FileField(required=False)
