from django.shortcuts import render

from django.views.generic import FormView
from django.template.loader import get_template
from django.http import HttpResponse
from rh.models import Person
from rh.forms import UnboardingForm

class UnboardingView(FormView):
    template_name = 'unboarding.html'
    form_class = UnboardingForm
    success_url = '/rh/unboarding/'

    def form_valid(self, form):
        # Enregistrer la personne dans la base de données
        personne = form.save()

        # Créer le PDF en utilisant un modèle
        template = get_template('unboarding_template.html')
        context = {
            'personne': personne,
        }
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="unboarding.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)

        # Retourner la réponse avec le PDF
        return response
