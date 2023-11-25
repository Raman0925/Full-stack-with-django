
from django.urls import path,include
from vid_Encoder import views
urlpatterns = [
    
    path('hello/',views.index)

]