from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def greet(request):
    date =datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = '<h1>Hello Friend, '
    if h<12:
        msg = msg+'Good Morning'
    elif h<16:
        msg = msg+'Good Afternoon'
    elif h<20:
        msg = msg + 'Good Evening'
    else:
        msg = msg + 'good night'
    msg = msg + '</h1><hr>'
    return HttpResponse(msg)

