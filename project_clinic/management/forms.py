from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from management.models import Medecin, RendezVous, Patient

SPECIALITE_CHOICES = [
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

    specialite = forms.ChoiceField(choices=SPECIALITE_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 150px;' 'display: inline-block;'}))
    class Meta:
        model = Medecin
        fields = "__all__"
        widgets = {
            'date_naissance': forms.DateInput(format=('%m/%d/%Y'), attrs={ 'placeholder':'Select a date', 'type':'date', 'style': 'width: 150px;'}),
        }

class RendezVousForm(ModelForm):

    type_rendez_vous = forms.ChoiceField(choices=TYPE_RDV_COICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 200px;' 'display: inline-block;'}))
    class Meta:
        model = RendezVous
        fields = ["medecin", "patient", "date_rendez_vous", "heure_debut", "type_rendez_vous"]
        widgets = {
            'date_rendez_vous': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date', 'style': 'width: 200px;' 'display: inline-block;'}),
            'heure_debut': forms.TimeInput(attrs={'type': 'time'}),
        }

class PatientForm(forms.ModelForm):
 class Meta:
    model = Patient
    fields = ('nom','prenom','date_naissance','numero_telephone','email')

    widgets = {
            'date_naissance': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'datep', 'placeholder':'Select a date', 'type':'date', 'style': 'width: 150px;'}),
        }
 def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prenom'].widget = forms.TextInput(attrs={'class': 'pren'})
        self.fields['nom'].widget = forms.TextInput(attrs={'class': 'nomp'})
        #self.fields['date_naissance'].widget = forms.DateInput(attrs={'class': 'datep'})
        self.fields['numero_telephone'].widget = forms.TextInput(attrs={'class': 'numtel'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'emailp'})