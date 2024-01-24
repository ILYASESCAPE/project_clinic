from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("medecin/", views.medecin, name="medecin"),
    path("patient/", views.patient, name="patient"),
]