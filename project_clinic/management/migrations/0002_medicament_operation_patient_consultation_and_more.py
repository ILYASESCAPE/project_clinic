# Generated by Django 5.0.1 on 2024-01-24 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id_medicament', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('dosage', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id_operation', models.AutoField(primary_key=True, serialize=False)),
                ('resulat', models.TextField(max_length=255)),
                ('suivi_postoperatoire', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id_patient', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('date_naissance', models.DateField(default='2000-01-01')),
                ('numero_telephone', models.CharField(max_length=15)),
                ('email', models.EmailField(default='default@example.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id_consultation', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_consultation', models.IntegerField(default=0)),
                ('diagnosis', models.CharField(max_length=100)),
                ('Traitement', models.CharField(max_length=100)),
                ('Medicaments', models.ManyToManyField(blank=True, to='management.medicament')),
            ],
        ),
        migrations.CreateModel(
            name='DossierMedical',
            fields=[
                ('id_dossier', models.AutoField(primary_key=True, serialize=False)),
                ('diagnosis', models.TextField(blank=True, null=True)),
                ('prescription', models.TextField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('Allergie', models.TextField(blank=True, null=True)),
                ('Medicaments', models.ManyToManyField(blank=True, to='management.medicament')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patient')),
            ],
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id_rendezvous', models.AutoField(primary_key=True, serialize=False)),
                ('date_rendez_vous', models.DateField()),
                ('heure_debut', models.TimeField()),
                ('consultation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.consultation')),
                ('medecin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.medecin')),
                ('operation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.operation')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patient')),
            ],
        ),
    ]