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
    path = "./support/templates/docs/franprix"
    file_names = os.listdir(path)

    return render(request, 'franprix.html', {'file_names': file_names})

def naturalia_files(request):
    path = "./support/templates/docs/naturalia"
    file_names = os.listdir(path)

    return render(request, 'naturalia.html', {'file_names': file_names})

def monoprix_files(request):
    path = "./support/templates/docs/monoprix"
    file_names = os.listdir(path)

    return render(request, 'monoprix.html', {'file_names': file_names})

def carrefour_files(request):
    path = "./support/templates/docs/carrefour"
    file_names = os.listdir(path)

    return render(request, 'carrefour.html', {'file_names': file_names})

def auchan_files(request):
    path = "./support/templates/docs/auchan"
    file_names = os.listdir(path)

    return render(request, 'auchan.html', {'file_names': file_names})


def download_pdf(request, name):
    # specify the paths to the PDF files
    file_path = 'support/templates/docs/' + name 

    # create a list of FileResponse objects
    response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{file_path.split("/")[-1]}"'
    
    return response
# return the list of FileResponse objects

