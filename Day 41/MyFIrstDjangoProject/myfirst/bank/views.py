from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    print(type(request))
    s = '<h1>Welcome to django classes</h1>'
    return HttpResponse(s)

def get_Time(request):
    time = datetime.datetime.now()
    s = "<h1>Hello current date time "+str(time)+"</h1>"
    return HttpResponse(s)

