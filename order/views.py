from django.shortcuts import render
from django.contrib import auth  
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf

from order.forms.order_form import OrderForm
from order.models.order import Orders



def order_index(request):
	return HttpResponseRedirect('/order/when/')

def order(request):
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			order = form.save()
			return HttpResponseRedirect('/order/when/')
	else:
		form = OrderForm()
	return render(request, 'order/when.html',locals())

