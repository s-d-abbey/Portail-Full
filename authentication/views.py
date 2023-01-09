from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.views.generic import View

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
    return render(request, 'home.html')