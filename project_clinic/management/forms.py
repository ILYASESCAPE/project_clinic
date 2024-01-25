from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from management.models import Medecin, RendezVous

SPECIALITE_CHOICES = [
    ("default", "---"),
    ("Cardiologue", "Cardiologue"),
    ("Neurologue", "Neurologue"),
    ("Urologue", "Urologue"),
    ("Rhumatologue", "Rhumatologue"),
    ("ORL", "ORL"),
    ("Generaliste", "Generaliste"),
]
TYPE_RDV_COICES =[
    ("Consultation", "Consultation"),
    ("Operation", "Operation"),
]

class medecinForm(ModelForm):

    #date_naissance_medecin = forms.DateField(widget=forms.DateInput)
    #specialite = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SPECIALITE_CHOISES)
    specialite = forms.ChoiceField(choices=SPECIALITE_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 200px;' 'border: solid;' 'margin: 50px;'}))
    class Meta:
        model = Medecin
        #fields = ["nom", "prenom", "email"]
        fields = "__all__"
        widgets = {
            'date_naissance': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date', 'style': 'width: 200px;'}),
            #'specialite': forms.CheckboxSelectMultiple,
        }

class RendezVousForm(ModelForm):
    type_rendez_vous = forms.ChoiceField(choices=TYPE_RDV_COICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    class Meta:
        model = RendezVous
        fields = ["medecin", "patient", "date_rendez_vous", "heure_debut", "type_rendez_vous"]
        #fields = "__all__"
        widgets = {
            'date_rendez_vous': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date', 'style': 'width: 200px;'}),
            'heure_debut': forms.TimeInput(attrs={'type': 'time'}),
        }