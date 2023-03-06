from django.contrib import admin
from django.urls import include, path

from rh import views

urlpatterns = [
    path('unboarding/', views.UnboardingView.as_view, name='unboarding'),
]