from django.db import models

class Person(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_arrivee = models.DateField(blank=True, null=True)
    service = models.CharField(max_length=50, choices=(
        ('superviseur', 'Superviseur'),
        ('paie', 'Paie'),
        ('comptabilite', 'Comptabilit√©'),
        ('informatique', 'Informatique'),
        ('autres', 'Autres'),
    ))
    droits = models.CharField(max_length=50, choices=(
        ('comptabilite', 'Comptabilit√©'),
        ('paie', 'Paie'),
        ('direction', 'Direction'),
    ), blank=True)
