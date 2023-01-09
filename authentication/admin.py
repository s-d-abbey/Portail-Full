from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Direction)
admin.site.register(Superviseur)
admin.site.register(Comptabilite)
admin.site.register(Magasin)
admin.site.register(RH)