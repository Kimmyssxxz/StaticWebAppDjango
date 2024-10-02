from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='students_home'),
    path('about/', views.about, name='students_about'),
    path('contact/', views.contact, name='students_contact'),
]
