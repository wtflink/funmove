from django.shortcuts import render
from django.contrib.staticfiles import finders
from os import listdir

def home(request):
	real_main_slider_path = finders.find('images/main-slider/')
	files = [f for f in listdir(real_main_slider_path)]
	main_slider_files = ['images/main-slider/' + f for f in files]
	context = {
		'main_sliders': main_slider_files
	}
	return render(request, 'home.html', context)