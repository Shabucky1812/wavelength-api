from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view()),
]
