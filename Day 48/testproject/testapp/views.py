from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"testapp/index.html")


def message(request):
    message = "Django Movie News"
    list_item1 = 'Krishna'
    list_item2 = 'Ganesh'
    mydict = {'message': message,"list1" : list_item1,"list2" : list_item2}
    return render(request,'testapp/news.html',mydict)