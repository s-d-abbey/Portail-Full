from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Sum
from django.db.models.functions import ExtractWeek
from django.shortcuts import redirect, render
from matplotlib.style import context

from authentication.models import *
from magboard.forms import MagasinForm

from .models import Magasin_value, Magasin_weekly


@login_required(login_url='login')
def historiqueView(request):
    if request.user.role == "MAGASIN":
        magasin_obj = Magasin_weekly.objects.filter(magasin__user=request.user)
        page = request.GET.get('page', -1)
       
       
        value = Magasin_value.objects.filter(magasin__user=request.user)
        rough_week_list = []
       
        for item in value:
            week = item.week
            rough_week_list.extend([week])
       
        week_list = []
        for week in rough_week_list:
            if week not in week_list:
                week_list.append(week)
       
        wvalue_list = []
        for w in week_list:
            magasine = Magasin_value.objects.filter(magasin__user=request.user, week=w)
        
            wvalue = magasine.aggregate(Sum('value'))
          
            final = {'week': w,
                'value': wvalue   
                }
            
            wvalue_list.append(final)
       
        value_list = []
        for val in value:
            value_list.extend([val.value])
        
        paginator = Paginator(magasin_obj, 1)
        try:
            magasin = paginator.page(page)
            
        except PageNotAnInteger:
            magasin = paginator.page(1)
        except EmptyPage:
            magasin = paginator.page(paginator.num_pages)
        
        return render(request, 'historique.html', {'magasins': magasin, 'magasin_value': value, 'total_magasin_value': wvalue_list})
    if request.user.role == "ADMIN" or request.user.is_staff or request.user.role == "DIRECTION":
        magasin_obj = Magasin.objects.all()
        
        page = request.GET.get('page', -1)
        mvalue = []
        wvalue = []


        









        for item in magasin_obj:
            value = Magasin_value.objects.filter(magasin=item)
            mvalue += value
            
            week_value = Magasin_weekly.objects.filter(magasin=item)
            wvalue += week_value
        

        rough_week_list = []
       
        for iteme in mvalue:
            week = iteme.week
            rough_week_list.extend([week])
       
        week_list = []
        for week in rough_week_list:
            if week not in week_list:
                week_list.append(week)
       
        wvalue_list = []
        for w in week_list:
            for pers in magasin_obj:
                magas = Magasin_value.objects.filter(magasin=pers, week=w)
        
                wwvalue = magas.aggregate(Sum('value'))
          
                final = {'mag': pers.user,
                    'week': w,
                    'value': wwvalue   
                    }
                
                wvalue_list.append(final)
        print(wvalue_list)






        paginator = Paginator(magasin_obj, 1)
        w_paginator = Paginator(wvalue, magasin_obj.count())
        try:
            magasin = paginator.page(page)
            w_magasin = w_paginator.page(page)
            
        except PageNotAnInteger:
            magasin = paginator.page(1)
            w_magasin = w_paginator.page(1)
        except EmptyPage:
            magasin = paginator.page(paginator.num_pages)
            w_magasin = w_paginator.page(w_paginator.num_pages)
        
        return render(request, 'historique.html', {'magasins': magasin, 'magasin_value': mvalue, 'magasin_weekly':w_magasin, 'total_magasin_value': wvalue_list})
    if request.user.role == "SUPERVISEUR":
        magasin_obj = Magasin.objects.filter(superviseur__user=request.user)
      
        page = request.GET.get('page', -1)
        mvalue = []
        wvalue = []
        for item in magasin_obj:
            value = Magasin_value.objects.filter(magasin=item)
            mvalue += value
            week_value = Magasin_weekly.objects.filter(magasin=item)
            wvalue += week_value
        paginator = Paginator(magasin_obj, 1)
        w_paginator = Paginator(wvalue, 1)
        try:
            magasin = paginator.page(page)
            w_magasin = w_paginator.page(page)
            
        except PageNotAnInteger:
            magasin = paginator.page(1)
            w_magasin = w_paginator.page(1)
        except EmptyPage:
            magasin = paginator.page(paginator.num_pages)
            w_magasin = w_paginator.page(w_paginator.num_pages)
        
        return render(request, 'historique.html', {'magasins': magasin, 'magasin_value': mvalue, 'magasin_weekly':wvalue})
    magasin = Magasin.objects.all()
    print(magasin)
    mvalue = []
    for item in magasin:
        value = Magasin_value.objects.filter(magasin=item)
        mvalue += value

    return render(request, 'historique.html', {'magasins': magasin, 'magasin_value': mvalue})

@login_required(login_url='login')
def formulaireView(request):
    magasin_u = Magasin.objects.get(user=request.user)
    if request.method == "POST":
        value = request.POST.get('magasin_value')    
        if Magasin_value.objects.filter(magasin=magasin_u, day=date.today()).exists():
            messages.error(request, "Vous avez déjà soumis aujourd'hui",
                           extra_tags='alert alert-warning alert-dismissible fade show')
            return redirect('historique')
        Magasin_value.objects.create(magasin=magasin_u, value=value)
        # if Magasin_weekly.objects.filter(magasin=magasin_u, week=date.today().isocalendar()[1]).exists():
        #     return redirect('historique')
        Magasin_weekly.objects.create(magasin=magasin_u, value=value)
        return redirect('historique')
    return render(request, 'formulaire.html')

@login_required(login_url='login')
def voirView(request, magasin, no):
    magasine = Magasin_weekly.objects.filter(magasin__user=magasin, week=no)
    # page = request.GET.get('page', no)
    # paginator = Paginator(magasine, 1)
    # try:
    #     magas = paginator.page(page)
    #     print(magas)
        
    # except PageNotAnInteger:
    #     magas = paginator.page(1)
    # except EmptyPage:
    #     magas = paginator.page(paginator.num_pages)
        
    value = Magasin_value.objects.filter(magasin__user=magasin)
    
    mag_user = Magasin.objects.get(user=magasin)
    return render(request, "voir.html", {'mag_user': mag_user, 'magasin': magasine, 'magasin_value': value})

@login_required(login_url='login')
def profileView(request):
    if request.user.role == "ADMIN":
        user = Admin.objects.get(user=request.user)
    if request.user.role == "DIRECTION":
        user = Direction.objects.get(user=request.user)
    if request.user.role == "SUPERVISEUR":
        user = Superviseur.objects.get(user=request.user)
    if request.user.role == "MAGASIN":
        user = Magasin.objects.get(user=request.user)
    if request.user.role == "RH":
        user = RH.objects.get(user=request.user)
    if request.user.role == "COMPTABILITE":
        user = Comptabilite.objects.get(user=request.user)

    return render(request, "profile.html", {'user': user})


