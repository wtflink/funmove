# -*- coding: utf-8 -*-
from django import forms
from order.models.order import Orders


class WhenForm(forms.ModelForm):
	class Meta:
		model = Orders
		fields = ['reservation_date', 'reservation_time', 'time_needed_hr', 'time_needed_min']
	
  

class WhereForm(forms.ModelForm):
	class Meta:
		model = Orders
		fields = [ 'departure', 'destination' ]