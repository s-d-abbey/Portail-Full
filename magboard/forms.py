from django import forms

from magboard.models import Magasin_value


class MagasinForm(forms.Form):
    class Meta:
        model = Magasin_value
        fields = ('value')
