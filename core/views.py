from django.shortcuts import render
from .models import Slideshow
# Create your views here.

def index (request):
    slideshow = Slideshow.objects.all()
	

	context={
	'slideshow':slideshow
    }
