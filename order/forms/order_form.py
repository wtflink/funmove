# -*- coding: utf-8 -*-
from django import forms
from order.models.order import Orders


class OrderForm(forms.ModelForm):
	class Meta:
		model = Orders
		fields = ['reservation_date', 'reservation_time',
		 'time_needed_hr', 'time_needed_min',
		 'departure', 'destination',
		 'name', 'email', 'cell_phone', 'birth_year', 'birth_month', 'birth_day', 'remarks']