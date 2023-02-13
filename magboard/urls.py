from django.contrib import admin
from django.urls import include, path

from magboard import views

urlpatterns = [
    path('historique/', views.historiqueView, name='historique'),
    path('formulaire/', views.formulaireView, name='formulaire'),
    path('historique/voir/<str:magasin>/<int:no>', views.voirView, name="voir"),
    
    path('historique/profile', views.profileView, name="user_profile"),  
    path('update_value/<int:week>', views.update_value, name="update_value")  
]