from django.shortcuts import render
from .forms import medecinForm, RendezVousForm

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
            
            # return redirect("listing") # redirection vers la page de l’url: listing
            #return render(request,"create.html",{"form":form,"message":mssg})
    else:
            form = medecinForm() 
            mssg ="veuillez remplir tous les champs"
            #return render(request,"create.html",{"form":form,"message ":mssg})
    context = {'form':form, "message":mssg}
    return render(request, "medecin.html", context) 

def patient(request):
    return render(request, "patient.html")


def RendezVous(request):
    #rendez_vouss = RendezVous.object.filter()
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            form = RendezVousForm()
            mssg="le rendez vous a ete ajouter"
            
            # return redirect("listing") # redirection vers la page de l’url: listing
            #return render(request,"create.html",{"form":form,"message":mssg})
    else:
            form = RendezVousForm() 
            mssg ="veuillez remplir tous les champs"
            #return render(request,"create.html",{"form":form,"message ":mssg})
    context = {'form':form, "message":mssg}
    return render(request, "rendez_vous.html", context) 