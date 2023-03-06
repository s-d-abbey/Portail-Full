from django.contrib import admin

from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    #list_display = ('username','fullname','role','email','id',)
    ordering = ('username',)
admin.site.register(User, UserAdmin)

class AdminAdmin(admin.ModelAdmin):
    list_display = ('username','fullname','role','email','id',)
    ordering = ('username',)
admin.site.register(Admin, AdminAdmin)

class DirectionAdmin(admin.ModelAdmin):
    list_display = ('username','fullname','role','email','id',)
    ordering = ('username',)
admin.site.register(Direction, DirectionAdmin)

class SuperviseurAdmin(admin.ModelAdmin):
    list_display = ('username','fullname','role','email','id',)
    ordering = ('username',)
admin.site.register(Superviseur, SuperviseurAdmin)

class ComptabiliteAdmin(admin.ModelAdmin):
    list_display = ('username','fullname','role','email','id',)
    ordering = ('username',)
admin.site.register(Comptabilite,ComptabiliteAdmin)

class JuristeAdmin(admin.ModelAdmin):
    list_display = ('username','fullname','role','email','id',)
    ordering = ('username',)
admin.site.register(Juriste,JuristeAdmin)

class RhAdmin(admin.ModelAdmin):
    list_display = ('username','fullname','role','email','id',)
    ordering = ('username',)
admin.site.register(RH,RhAdmin)

class MagasinAdmin(admin.ModelAdmin):
    list_display = ('code','user','fullname', 'role','enseignes','email','id',)
    ordering = ('code',)
admin.site.register(Magasin, MagasinAdmin)

