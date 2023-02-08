from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.views.generic import View
from authentication.models import Magasin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Sum
from magboard.models import Magasin_day_value, Magasin_value, Magasin_weekly

from . import forms

# def signup_page(request):
#     form = forms.SignupForm()
#     if request.method == 'POST':
#         form = forms.SignupForm(request.POST)   
#         if form.is_valid():
#             user = form.save()
#             # auto-login user
#             login(request, user)
#             return redirect(settings.LOGIN_REDIRECT_URL)
#     return render(request, 'authentication/signup.html', context={'form': form})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "informations d'identification d'utilisateur erronées",
                               extra_tags='alert alert-warning alert-dismissible fade show')
    return render(request, 'authentication/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    

        magasin_obj = Magasin_day_value.objects.all().order_by('magasin__code')

        ori_magasin = Magasin.objects.all().order_by('code')

        page = request.GET.get('page', -1)
        
       
        mvalue = []
        wvalue = []
        mdvalue = []
      





        for item in magasin_obj:
            magasin_day_value = Magasin_day_value.objects.filter(magasin=item.magasin)
            mdvalue += magasin_day_value
            value = Magasin_value.objects.filter(magasin=item.magasin)
            mvalue += value
            
            week_value = Magasin_weekly.objects.filter(magasin=item.magasin)
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
        other_mag = []
        for w in week_list:
            
            for pers in Magasin.objects.all():
                magas = Magasin_value.objects.filter(magasin=pers, week=w)
        
                wwvalue = magas.aggregate(Sum('value'))
          
                final = {'mag': pers.user,
                    'week': w,
                    'value': wwvalue   
                    }
                
                wvalue_list.append(final)
            null_magasin = ori_magasin.exclude(magasin_value__week=w)
            fin = {'week': w,
                'list': null_magasin}
            other_mag.append(fin)
        
       
        
        
    

        paginator = Paginator(magasin_obj, 1)
        w_paginator = Paginator(wvalue, 1)
        weekpaginator = Paginator(week_list, 1)
        wpage = request.GET.get('page', weekpaginator.num_pages)
   

        wlist = len(wvalue_list)
        return render(request, 'home.html', {'weekpag': weekpaginator})