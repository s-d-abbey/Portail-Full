from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path

import authentication.views
from authentication import views

from . import views as Appviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page,
        name='login'),

    #Authentication
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/', authentication.views.home, name='home'),

    #Magboard
    path('magboard/', include('magboard.urls')), 

    #Primweb
    path('primweb/', Appviews.primwebView, name='primweb'),

    #Comptabilite
    path('comptabilite/', Appviews.comptabiliteView, name='comptabilite'),

    #Support
    path('support/', Appviews.supportView, name='support'),

    #Paie
    path('paie/', Appviews.paieView, name='paie'),

]
