from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect




@login_required(login_url='login')
def primwebView(request):
    return render(request, 'app_templates/primweb.html')

@login_required(login_url='login')
def comptabiliteView(request):
    return render(request, 'app_templates/comptabilite.html')

@login_required(login_url='login')
def supportView(request):
    return render(request, 'app_templates/support.html')

@login_required(login_url='login')
def paieView(request):
    return render(request, 'app_templates/paie.html')
