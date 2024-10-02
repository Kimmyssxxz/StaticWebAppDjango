from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='courses_home'),
    path('enroll/', views.enroll, name='courses_enroll'),
    path('feedback/', views.feedback, name='courses_feedback'),
]
