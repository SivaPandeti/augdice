from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def pie(request):
    return render(request, 'charts/pie.html', {})