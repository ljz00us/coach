from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from models import coaches

# for finding city locations:
# put this on top
#
# from django.contrib.gis.utils import GeoIP
# ... then see http://stackoverflow.com/questions/2218093/django-retrieve-ip-location

# Create your views here.

def home(request):
    return render_to_response('home.html',{'coaches':coaches.objects.all()})

def results(request):
    return render_to_response('results.html',{'results':results})
