# -*- coding: utf-8 -*-
from django import forms

class backendImageForm(forms.Form):
	image = forms.FileField(label='Select a Image')