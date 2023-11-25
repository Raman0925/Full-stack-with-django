from django.urls import path,include
from lmvt_app import views
urlpatterns = [
    path('hello/', views.homepage)
]
