from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def medecin(request):
    return render(request, "main/medecin.html") 

def patient(request):
    return render(request, "patient.html")


def RendezVous(request):
    rendez_vouss = RendezVous.object.filter()