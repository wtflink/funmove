from django.shortcuts import render
from django.contrib import auth  
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf

from order.forms.order_form import WhenForm
from order.models.order import Orders



def order_index(request):
	return render(request,'order/when.html',locals())

def order_When(request):
	if request.method == 'POST':
		form = WhenForm(request.POST)
		if form.is_valid():
			order = form.save()
			return HttpResponseRedirect('/order/when/')
	else:
		form = WhenForm()
	return render(request, 'order/when.html',locals())