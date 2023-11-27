from django.urls import path
from marksapp import views
urlpatterns = [
    path('hello/',views.mark_view),
]


