from django.shortcuts import render
from django.contrib import auth  
from django.http.response import HttpResponseRedirect

# Create your views here.
def index(request):
 	return render_to_response('index.html',locals())

def login(request):
	context = {}

	 if request.user.is_authenticated(): 
        return render(request, 'backend/index.html', context)
   
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('backend/index.html')
    else:
        return render(request, 'backend/login.html', context) 