from django.shortcuts import render
import datetime

# Create your views here.
def mark_view(request):
    time =datetime.datetime.now()

    my_dict = {'time':time,
               'name':"django",
               'required':'python'
                 }
    
    return render(request,'marks_app/index.html',context=my_dict)