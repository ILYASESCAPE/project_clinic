from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Medecin(models.Model):
    id_medecin = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    specialite = models.CharField(max_length=50)
    numero_telephone = models.CharField(max_length=10)
    email = models.EmailField(default="default@example.com")
    def __str__(self):
        return self.nom
    
class Patient(models.Model):
    id_patient = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField(default='2000-01-01')
    numero_telephone = models.CharField(max_length=15)
    email = models.EmailField(default="default@example.com")

    def __str__(self):
        return self.nom
    

class Medicament(models.Model):
    id_medicament = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    dosage = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom

class Consultation(models.Model):
    id_consultation = models.AutoField(primary_key=True)
    nombre_consultation = models.IntegerField(default=0)
    diagnosis = models.CharField(max_length=100)
    Traitement = models.CharField(max_length=100)
    Medicaments = models.ManyToManyField(Medicament, blank=True)


class Operation(models.Model):
    id_operation = models.AutoField(primary_key=True)
    resulat = models.TextField(max_length=255)
    suivi_postoperatoire = models.TextField(max_length=255)


class DossierMedical(models.Model):
    id_dossier = models.AutoField(primary_key=True)
    diagnosis = models.TextField(blank=True, null=True)
    prescription = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now=True)
    Allergie = models.TextField(blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Medicaments = models.ManyToManyField(Medicament, blank=True)

    def __str__(self):
        return f"Dossier Medical de {self.patient.nom} {self.patient.prenom}"
    
class RendezVous(models.Model):
    id_rendezvous = models.AutoField(primary_key=True)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_rendez_vous = models.DateField()
    heure_debut = models.TimeField()
    type_rendez_vous = models.CharField(max_length=50)
    consultation = models.ForeignKey(Consultation,on_delete=models.CASCADE,null=True,blank=True)
    operation = models.ForeignKey(Operation,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"{self.id_rendezvous}"

    def verifie(self):
        if self.consultation and self.operation:
            raise ValidationError("On ne peut pas choisir à la fois consultation et opération")
        if not self.consultation and not self.operation:
            raise ValidationError("vous devez choisir soit la consultation, soit l'opération")