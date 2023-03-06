from django import forms
from rh.models import Person

class UnboardingForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('nom', 'prenom', 'date_arrivee', 'service', 'droits')
