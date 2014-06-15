from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import urllib2

def job(request):
	#return HttpResponse(urllib2.urlopen('https://api.dice.com/jobs/b912258f4891d5be053622dffcb7cbbd').read())
	return HttpResponse(urllib2.urlopen('api/getMarkers').read())
    #return render(request, 'mapview/googlemaps.html', {})

