# -*- coding: utf-8 -*-

from django import forms

from crispy_forms.helper import FormHelper

from .models import Reporte


class ReporteForm(forms.ModelForm):

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False
        helper.label_class = 'col-lg-4'
        helper.field_class = 'col-lg-8'

        return helper

    class Meta:
        model = Reporte
