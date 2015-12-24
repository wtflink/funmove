from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context,RequestContext
from django import forms
import hashlib, datetime, random
from django.utils import timezone

from order.forms.order_form import OrderForm
from order.models.schedule import Schedule,timeofaday
from order.models.order import Orders


def order_index(request):
	return HttpResponseRedirect('/order/when/')

def order(request):
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			#commit=false for the confirmationkey modification
			order = form.save(commit=False)

			sendto = form.cleaned_data['email']
			salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
			order.confirmation_key = hashlib.sha1(salt+sendto).hexdigest()
			order.key_expires = timezone.now() + datetime.timedelta(2)
			order.save()

			#save the time that has been reserved
			time =  timeofaday.objects.get(time = order.reservation_time)
			start = time.id
			n = order.time_needed_hr*2 + order.time_needed_min/30
			for i in range(start, start+n, 1):
				time.id = i
				Schedule.objects.create( reservation_date = order.reservation_date, reservation_time = time )

			#send a mail of the order information to the user by which email address they input
			#edit the template in the templates/order/email_template.txt to change the context of it
			text = get_template('order/email_template.txt')
			mailcont = Context({ 'order': order })
			text_content = text.render(mailcont)
			msg = EmailMultiAlternatives('ur order', text_content, 'wtflink515@gmail.com', [sendto])
			msg.send()

			return HttpResponseRedirect('/order/when')
	else:
		form = OrderForm()
	return render(request, 'order/order.html', locals())

def confirm(request, confirmation_key):
	if confirmation_key == 'done':
		raise Http404("the confirmation key does not exist")

	# check if there is Orders which matches the confirmation key (if not then display 404)
	order = get_object_or_404(Orders, confirmation_key=confirmation_key)

	#check if the confirmation key has expired, if it expired then render confirm_expired.html
	if order.key_expires < timezone.now():
		return render_to_response('order/confirm_expired.html', {'order' : order}, context_instance = RequestContext(request))

	#if the key hasn't expired, set the order confirmed and show user the order info again
	order.is_confirmed = True
	order.confirmation_key = 'done'
	order.save()
	return render_to_response('order/confirm.html', {'order' : order}, context_instance = RequestContext(request))


