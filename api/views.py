from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import urllib2

def getMarkers(request):
	json_file = 'tests/showMap_US.json'
	with open(json_file, 'r') as f:
		json = f.read()
	return HttpResponse(json)
    #return render(request, 'mapview/googlemaps.html', {})

def getPieData(request):
	#json_file = 'tests/pie.json'
	#with open(json_file, 'r') as f:
	#	json = f.read()
	json = urllib2.urlopen('https://api.dice.com/jobs?fields=id,company,position&page=1&q=ruby').read()
	return HttpResponse(json)

def getJobsData(request):
	#req = urllib2.Request('https://api.dice.com/jobs?fields=id,skills,position&page=1&q=ruby')
	req = urllib2.Request('https://api.dice.com/jobs?fields=id,skills,position&count=120&position.location.region=CA')
	#https://api.dice.com/jobs/c3fd6cce9c33584e758140e277dba5d1/recommendedJobs?fields=recommendationRating,job.id,job.company.name,job.position.location
	req.add_header('Authorization', 'bearer c50f0129-3d40-4de5-99e8-c00410421a2e')
	resp = urllib2.urlopen(req)
	json = resp.read()
	return HttpResponse(json)