from django.contrib import admin

from .models import Magasin_value, Magasin_weekly

# Register your models here.
admin.site.register(Magasin_weekly)
admin.site.register(Magasin_value)
