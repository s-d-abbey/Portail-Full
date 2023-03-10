from django.urls import path

from support import views

from . import views as Supportviews

urlpatterns = [
    path('docs/', Supportviews.supportView, name='support'),
    path('docs/franprix', Supportviews.franprix_files, name="franprix_files"),
    path('docs/autres', Supportviews.autres_files, name="autres_files"),
    path('docs/naturalia', Supportviews.naturalia_files, name="naturalia_files"),
    path('docs/monoprix', Supportviews.monoprix_files, name="monoprix_files"),
    path('docs/carrefour', Supportviews.carrefour_files, name="carrefour_files"),
    path('docs/auchan', Supportviews.auchan_files, name="auchan_files"),
    path('download_pdf/<str:dir_name>/<str:name>', Supportviews.download_pdf, name='download_pdf'),
    path('ticket/create/', views.ticket_create_view, name='ticket_create'),
    path('ticket/list/', views.ticket_list_view, name='ticket_list'),
]
