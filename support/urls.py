from django.urls import path



from . import views as Appviews

urlpatterns = [
    path('docs/', Appviews.supportView, name='support')
]
