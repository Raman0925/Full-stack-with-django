from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def IndiJobs(request):
    s="<h1>Welcome to Job portal</h1>"
    return HttpResponse(s)



