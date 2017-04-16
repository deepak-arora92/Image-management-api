# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    apikey = forms.CharField(max_length=6, min_length=6, required=True, label='api key')
    image = forms.FileField(
        label='Select a file',
        help_text='max. 5 MB'
    )