from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import os
from authentication.models import Magasin
from django.http import FileResponse
# Create your views here.

@login_required(login_url='login')
def supportView(request):
    if request.user.role == "MAGASIN":
        magasin = Magasin.objects.get(user=request.user)
        return render(request, 'support.html', {'magasin': magasin})
    return render(request, 'support.html')

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

