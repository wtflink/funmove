from django.shortcuts import render
from django.contrib import auth  
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required # @login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

    
def index(request):
	return render(request,'backend/index.html',locals())

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/backend/index/')

def login(request):

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

