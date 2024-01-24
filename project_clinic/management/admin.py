from django.contrib import admin
from .models import Medecin, Patient, DossierMedical, RendezVous, Operation, Consultation, Medicament

# Register your models here.


admin.site.register(Medecin)
admin.site.register(Patient)
admin.site.register(Medicament)
admin.site.register(Consultation)
admin.site.register(Operation)
admin.site.register(DossierMedical)
admin.site.register(RendezVous)
