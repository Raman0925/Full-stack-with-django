from django.urls import path
from dbapp import views
urlpatterns = [
    path('a/',views.index ),
]
