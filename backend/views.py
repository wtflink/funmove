# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import auth  
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required # @login_required
from django.contrib.auth.forms import UserCreationForm

from forms.image_form import backendImageForm
from models.image_model import backendImage

# Create your views here.

@login_required
def index(request):
	return render(request,'backend/index.html',locals())

@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/backend/index/')

def login(request):

	###{% if request.user.is_authenticated %} 
	###{% else %}
    ###  <p>you need to login!! <a href="{% url 'backend_login' %}"> login! </a></p>
    ###{% endif %} 

	if request.user.is_authenticated(): 
		return HttpResponseRedirect('/backend/index/')
   
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
    
	user = auth.authenticate(username=username, password=password)

	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/backend/index/')
	else:
		return render(request, 'backend/signin.html',locals()) 

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect('/backend/accounts/login/')
	else:
		form = UserCreationForm()
	return render(request, 'backend/register.html',locals())

@login_required 
def upload(request):
	# Handle file upload
	# utf-8 file name not supported
	if request.method == 'POST':
		form = backendImageForm(request.POST, request.FILES)
		if form.is_valid():
			newimg = backendImage(image = request.FILES['image'])
			newimg.save()
			return HttpResponseRedirect(reverse('backend_upload'))
	else:
		form = backendImageForm() # A empty, unbound form
	documents = backendImage.objects.all()
	return render_to_response(
		'backend/image_form.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)

@login_required
def imgDel(request,pk):
	img = backendImage.objects.get(pk=pk)
	img.delete()
	form = backendImageForm()
	documents = backendImage.objects.all()
	return render_to_response(
		'backend/image_form.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)