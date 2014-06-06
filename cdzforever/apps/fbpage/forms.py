# -*- coding: utf-8 -*-

from django import forms
from django.forms.formsets import formset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


def helper():
    helper = FormHelper()
    helper.form_tag = False
    helper.template = 'bootstrap3/table_inline_formset.html'
    helper.add_input(Submit("submit", "Save"))

    return helper


class AgendarForm(forms.Form):
    texto = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
    datahora = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': '%Y-%m-%d %H:%M'}))
    imagem = forms.FileField()

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False
        helper.add_input(Submit("submit", "Save"))

        return helper


AgendarFormSet = formset_factory(AgendarForm, extra=5)
AgendarFormSet.helper = helper()
