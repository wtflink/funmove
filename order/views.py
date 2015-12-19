from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django import forms

from order.forms.order_form import OrderForm
from order.models.schedule import Schedule,timeofaday
from order.models.order import Orders


def order_index(request):
	return HttpResponseRedirect('/order/when/')

def order(request):
	args = {}
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			
			order = form.save()
			#save the time that has been reserved
			time =  timeofaday.objects.get(time = order.reservation_time)
			start = time.id
			n = order.time_needed_hr*2 + order.time_needed_min/30
			for i in range(start, start+n, 1):
				time.id = i
				Schedule.objects.create( reservation_date = order.reservation_date, reservation_time = time )

			#send a mail of the order information to the user by which email address they input
			#edit the template in the templates/order/email_template.txt to change the context of it
			send_to = form.cleaned_data['email']
			text = get_template('order/email_template.txt')
			mailcont = Context({ 'order': order })
			text_content = text.render(mailcont)
			msg = EmailMultiAlternatives('ur order', text_content, 'whatever@gmail.com', [send_to])
			msg.send()

			return HttpResponseRedirect('/order/when')
	else:
		form = OrderForm()
	args['form'] = form	
	return render(request, 'order/order.html', args)

