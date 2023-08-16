from django.urls import path
from . import views

urlpatterns = [
    path('tracks/', views.TrackList.as_view()),
]
