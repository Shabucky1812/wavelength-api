from django.urls import path
from . import views

urlpatterns = [
    path('tracks/', views.TrackList.as_view()),
    path('tracks/<int:id>/', views.TrackDetail.as_view()),
]
