from django import forms

from magboard.models import Magasin_value
from .widget import DatePickerInput

class MagasinForm(forms.Form):
    day = forms.DateField(label='Date of Birth', widget=DatePickerInput())
    class Meta:
        model = Magasin_value
        fields = ['nom', 'prenom', 'clients_no', 'day', 'value']
