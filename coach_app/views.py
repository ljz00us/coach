from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from sort import print_coach

# for finding city locations:
# put this on top
# from django.contrib.gis.utils import GeoIP
# ... then see http://stackoverflow.com/questions/2218093/django-retrieve-ip-location
# Create your views here.

def home(request):
    return render_to_response('home.html')

def results(request):
    # data = {'results':print_coach() }
    return render(request, 'results.html')

def coach_home(request):
    return render(request, 'coach_home.html')

def jan(request):
    return render(request, 'jan.html')