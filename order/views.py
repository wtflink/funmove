from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf

from order.forms.order_form import OrderForm
from order.models.schedule import Schedule,timeofaday
from order.models.order import Orders
from django.core.mail import send_mail



def order_index(request):
	return HttpResponseRedirect('/order/when/')

def order(request):
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

			#mailling test
			send_mail('ur time order', 'test', 'wtflink515@gmail.com', ['wtflink515@gmail.com'], fail_silently=False)

			return HttpResponseRedirect('/order/when/')
	else:
		form = OrderForm()
	return render(request, 'order/when.html',locals())

