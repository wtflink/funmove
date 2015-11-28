# -*- coding: utf-8 -*-
from django import forms
from order.models.order import Orders


class OrderForm(forms.ModelForm):
	class Meta:
		model = Orders
		# Show field on th form
		fields = [
			'reservation_date', 'reservation_time', 'departure',
			'destination']