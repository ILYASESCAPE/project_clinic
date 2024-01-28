from django.shortcuts import render
from .forms import medecinForm, RendezVousForm, PatientForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def medecin(request):
    
    if request.method == 'POST':
        form = medecinForm(request.POST)
        if form.is_valid():
            form.save()
            form = medecinForm()
            mssg="le medecin a ete ajouter"
    else:
            form = medecinForm() 
            mssg ="veuillez remplir tous les champs"
    context = {'form':form, "message":mssg}
    return render(request, "medecin.html", context) 

def RendezVous(request):
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            form = RendezVousForm()
            mssg="le rendez vous a ete ajouter"      
    else:
            form = RendezVousForm() 
            mssg ="veuillez remplir tous les champs"
    context = {'form':form, "message":mssg}
    
    return render(request, "rendez_vous.html", context) 

def patientCreate(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            form = PatientForm()
            mssg="le patient a ete ajouter"      
    else:
            form = PatientForm() 
            mssg ="veuillez remplir tous les champs"
    context = {'form':form, "message":mssg}
    
    return render(request, "patient.html", context) 