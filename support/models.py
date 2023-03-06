from django.db import models

# Create your models here.
class Ticket(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    
