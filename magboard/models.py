import datetime
from datetime import date

from django.db import models

from authentication.models import Magasin


# Create your models here.
class Magasin_weekly(models.Model):
    magasin = models.ForeignKey(Magasin, on_delete=models.CASCADE)
    value = models.IntegerField()
    week = models.IntegerField(default=date.today().isocalendar()[1])
    
    
    def __str__(self):
        return f"{self.magasin.user} - {self.week}"

class Magasin_value(models.Model):
    magasin = models.ForeignKey(Magasin,  on_delete=models.CASCADE)
    value = models.IntegerField()
    day = models.DateField(default=date.today)
    week = models.IntegerField(default=date.today().isocalendar()[1])
    class Meta:
        ordering = ['day']
    def name_of_day(self):
        if self.day.isoweekday() == 7:
            return "Dimanche"
        if self.day.isoweekday() == 6:
            return "Samedi"
        if self.day.isoweekday() == 5:
            return "Vendredi"
        if self.day.isoweekday() == 4:
            return "Jeudi"
        if self.day.isoweekday() == 3:
            return "Mercredi"
        if self.day.isoweekday() == 2:
            return "Mardi"
        if self.day.isoweekday() == 1:
            return "Lundi"
        
   
    def __str__(self):
        if self.day.isoweekday() == 7:
            day_name = "Dimanche"
        if self.day.isoweekday() == 6:
            day_name = "Samedi"
        if self.day.isoweekday() == 5:
            day_name = "Vendredi"
        if self.day.isoweekday() == 4:
            day_name = "Jeudi"
        if self.day.isoweekday() == 3:
            day_name = "Mercredi"
        if self.day.isoweekday() == 2:
            day_name = "Mardi"
        if self.day.isoweekday() == 1:
            day_name = "Lundi"
        
        return f"{self.magasin.user} - {self.week} - {day_name} - {self.value}"


