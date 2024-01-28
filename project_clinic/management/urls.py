from django.urls import path
from . import views

urlpatterns = [
    path("medecin/", views.medecin, name="medecin"),
    path("patient/", views.patientCreate, name="patient"),        
    path("rendez_vous/", views.RendezVous, name="rendez_vous"), 
]