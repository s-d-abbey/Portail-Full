from django import forms
from .models import Ticket

from django import forms

class TicketForm(forms.Form):
    TYPE_CHOICES = (
        ('Incident', 'Incident'),
        ('Demande', 'Demande'),
    )
    URGENCY_CHOICES = (
        ('Basse', 'Basse'),
        ('Normal', 'Normal'),
        ('Haute', 'Haute'),
    )
    type = forms.ChoiceField(choices=TYPE_CHOICES)
    urgency = forms.ChoiceField(choices=URGENCY_CHOICES)
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
