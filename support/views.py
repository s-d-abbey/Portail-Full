from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import os
from authentication.models import Magasin
from django.http import FileResponse

from .forms import TicketForm
# Create your views here.

@login_required(login_url='login')
def supportView(request):
    if request.user.role == "MAGASIN":
        magasin = Magasin.objects.get(user=request.user)
        return render(request, 'support.html', {'magasin': magasin})
    return render(request, 'support.html')

def autres_files(request):
    path = "/home/adminunifrais/Documents/Portail/Autres/"
    file_names = os.listdir(path)
    dir_name = "Autres"
    return render(request, 'autres.html', {'file_names': file_names, 'dir_name': dir_name})

def franprix_files(request):
    path = "/home/adminunifrais/Documents/Portail/Franprix"
    file_names = os.listdir(path)
    dir_name = "Franprix"
    return render(request, 'franprix.html', {'file_names': file_names, 'dir_name': dir_name})

def naturalia_files(request):
    path = "/home/adminunifrais/Documents/Portail/Naturalia"
    file_names = os.listdir(path)
    dir_name = "Naturalia"
    return render(request, 'naturalia.html', {'file_names': file_names, 'dir_name': dir_name})

def monoprix_files(request):
    path = "/home/adminunifrais/Documents/Portail/Monoprix"
    file_names = os.listdir(path)
    dir_name = "Monoprix"
    return render(request, 'monoprix.html', {'file_names': file_names, 'dir_name': dir_name})

def carrefour_files(request):
    path = "/home/adminunifrais/Documents/Portail/Carrefour"
    file_names = os.listdir(path)
    dir_name = "Carrefour"
    return render(request, 'carrefour.html', {'file_names': file_names, 'dir_name': dir_name})

def auchan_files(request):
    path = "/home/adminunifrais/Documents/Portail/Auchan"
    file_names = os.listdir(path)
    dir_name = "Auchan"
    return render(request, 'auchan.html', {'file_names': file_names, 'dir_name': dir_name})


def download_pdf(request, name, dir_name):
    # specify the paths to the PDF files
    file_path = '/home/adminunifrais/Documents/Portail/'+ dir_name + "/" + name 
    # create a list of FileResponse objects
    response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{file_path.split("/")[-1]}"'
    
    return response
# return the list of FileResponse objects

#def glpi(request):
#    return render(request, 'glpi.html')


def ticket_create_view(request):
    form = TicketForm(request.POST or None)
    if form.is_valid():
        # Récupération des données du formulaire
        type = form.cleaned_data['type']
        urgency = form.cleaned_data['urgency']
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        
        # Construction de la requête à l'API de GLPI
        api_url = 'http://192.1.200.183/glpi/apirest.php'
        api_key = 'xiRFOa1HdYddELXizs6Lfu62lAHQtvk1jciu7lZJ'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + api_key,
        }
        data = {
            'input': {
                'name': title,
                'content': description,
                'urgency': urgency,
                'type': type,
                'users_id': request.user.id,
            }
        }
        response = requests.post(api_url + '/Ticket', headers=headers, json=data)
        
        # Vérification de la réponse
        if response.status_code == 201:
            # Redirection vers une page de confirmation
            return render(request, 'ticket_created.html')
    
    # Affichage du formulaire
    context = {
        'form': form,
    }
    return render(request, 'ticket.html', context)



def ticket_list_view(request):
    # Récupération des tickets en cours
    api_url = 'http://192.1.200.183/glpi/apirest.php'
    api_key = 'xiRFOa1HdYddELXizs6Lfu62lAHQtvk1jciu7lZJ'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + api_key,
    }
    params = {
        'criteria': {
            'status': '2', # 2 = en cours
        },
        'forcedisplay': {
            '0': 'name',
            '1': 'urgency',
            '2': 'status',
        }
    }
    response = requests.get(api_url + '/Ticket', headers=headers, params=params)
    
    # Affichage des tickets en cours
    tickets = response.json()
    context = {
        'tickets': tickets['data'],
    }
    return render(request, 'ticket_list.html', context)
