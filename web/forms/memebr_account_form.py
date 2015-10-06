# -*- coding: utf-8 -*-
from django import forms
from web.models.member import MemberAccount



class MemberAccountForm(forms.ModelForm):
	class Meta:
		model = MemberAccount
		# Show field on th form
		fields = [
			'account', 'email', 'password',
			'birth_year', 'birth_month', 'birth_day',
			'contact_email', 'face_image',
			'content', 'youtube_url', 'topic_num']