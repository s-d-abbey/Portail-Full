from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    
    ADMIN = 'ADMIN'
    DIRECTION = 'DIRECTION'
    SUPERVISEUR = 'SUPERVISEUR'
    COMPTABILITE = 'COMPTABILITE'
    PAIE = 'PAIE'
    MAGASIN = 'MAGASIN'
    RH = 'RH'

    ROLE_CHOICES=(
        (ADMIN, 'ADMIN'),
        (DIRECTION, 'DIRECTION'),
        (SUPERVISEUR, 'SUPERVISEUR'),
        (COMPTABILITE, 'COMPTABILITE'),
        (PAIE, 'PAIE'),
        (MAGASIN, 'MAGASIN'),
        (RH, 'RH'),
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='ROLE')
    code = models.CharField(max_length=3)

          
class Admin(models.Model):
    ADMIN = 'ADMIN'
    ROLE_CHOICES=(
        ("", '----'),
        (ADMIN, 'ADMIN')
    )

    user = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="ADMIN")
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    number = PhoneNumberField(null=False, blank=False)

    def __str__(self):
        return self.user
    

    @receiver(post_save, sender="authentication.Admin")
    def addGroup(sender, instance, created, **kwargs):
        if created:
            if instance.role == "ADMIN":
                User.objects.create_user(username=instance.user, role=instance.role, password=instance.password, email=instance.email, is_staff=True)
                admin_permission = Permission.objects.filter(name__contains="view admin")
                comptabilite_permission = Permission.objects.filter(name__contains="comptabilite")
                direction_permission = Permission.objects.filter(name__contains="direction")
                magasin_permission = Permission.objects.get(name="Can view magasin")
                magboard_permission = Permission.objects.get(name="Can view magasin_value")
                superviseur_permission = Permission.objects.get(name="Can view superviseur")
                user = User.objects.get(username=instance.user)
                user.user_permissions.add(*admin_permission)
                user.user_permissions.add(*comptabilite_permission)
                user.user_permissions.add(*direction_permission)
                user.user_permissions.add(magasin_permission)
                user.user_permissions.add(magboard_permission)
                user.user_permissions.add(superviseur_permission)
    @receiver(pre_delete, sender="authentication.Admin")
    def delete_user(sender, instance, **kwargs):
       
            if User.objects.filter(username=instance.user, role=instance.role).exists():
                user = User.objects.get(username=instance.user, role=instance.role)
                user.delete()

           
class Direction(models.Model):
    DIRECTION = 'DIRECTION'
    ROLE_CHOICES=(
        ("", '----'),
        (DIRECTION, 'DIRECTION')
    )
    user = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="DIRECTION")
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    number = PhoneNumberField(null=False, blank=False)
    def __str__(self):
        return self.user

    @receiver(post_save, sender="authentication.Direction")
    def addGroup(sender, instance, created, **kwargs):
        if created:
            if instance.role == "DIRECTION":
                User.objects.create_user(username=instance.user, role=instance.role, email=instance.email, password=instance.password)

    @receiver(pre_delete, sender="authentication.Direction")
    def delete_user(sender, instance, **kwargs):
       
            if User.objects.filter(username=instance.user, role=instance.role).exists():
                user = User.objects.get(username=instance.user, role=instance.role)
                user.delete()


class Comptabilite(models.Model):
    COMPTABILITE = 'COMPTABILITE'
    ROLE_CHOICES=(
        ("", '----'),
        (COMPTABILITE, 'COMPTABILITE')
    )
    user = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="COMPTABILITE")
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    number = PhoneNumberField(null=False, blank=False)
    def __str__(self):
        return self.user

    @receiver(post_save, sender="authentication.Comptabilite")
    def addGroup(sender, instance, created, **kwargs):
        if created:
            if instance.role == "COMPTABILITE":
                User.objects.create_user(username=instance.user, role=instance.role, email=instance.email, password=instance.password)
    
    @receiver(pre_delete, sender="authentication.Comptabilite")
    def delete_user(sender, instance, **kwargs):
       
            if User.objects.filter(username=instance.user, role=instance.role).exists():
                user = User.objects.get(username=instance.user, role=instance.role)
                user.delete()

                
class Magasin(models.Model):
    MAGASIN = 'MAGASIN'
    ROLE_CHOICES=(
        ("", '----'),
        (MAGASIN, 'MAGASIN')
    )
    code = models.CharField(max_length=3)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="MAGASIN")
    superviseur = models.ForeignKey("Superviseur", related_name="My_Superviseur", on_delete=models.SET_NULL, null=True,  blank=True)
    email = models.EmailField(max_length=254)
    number = PhoneNumberField(null=False, blank=False)
    
    def __str__(self):
        return self.user

   
    @receiver(post_save, sender="authentication.Magasin")
    def addGroup(sender, instance, created, **kwargs):
        if created:
            if instance.role == "MAGASIN":
                User.objects.create_user(code=instance.code,username=instance.user, role=instance.role, email=instance.email, password=instance.password)

    @receiver(pre_delete, sender="authentication.Magasin")
    def delete_user(sender, instance, **kwargs):
       
            if User.objects.filter(username=instance.user, role=instance.role).exists():
                user = User.objects.get(username=instance.user, role=instance.role)
                user.delete()
    

class Superviseur(models.Model):
    SUPERVISEUR = 'SUPERVISEUR'
    ROLE_CHOICES=(
        ("", '----'),
        (SUPERVISEUR, 'SUPERVISEUR')
    )
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="SUPERVISEUR")
    magasin = models.ManyToManyField(Magasin, related_name="Magasins", blank=True)
    email = models.EmailField(max_length=254)
    number = PhoneNumberField(null=False, blank=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.user

    @receiver(post_save, sender="authentication.Superviseur")
    def addGroup(sender, instance, created, **kwargs):
        if created:
            if instance.role == "SUPERVISEUR":
                User.objects.create_user(username=instance.user, role=instance.role, email=instance.email, password=instance.password)

    @receiver(pre_delete, sender="authentication.Superviseur")
    def delete_user(sender, instance, **kwargs):
       
            if User.objects.filter(username=instance.user, role=instance.role).exists():
                user = User.objects.get(username=instance.user, role=instance.role)
                user.delete()


class RH(models.Model):
    RH = 'RH'
    ROLE_CHOICES=(
        ("", '----'),
        (RH, 'RH')
    )
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="RH")
    
    email = models.EmailField(max_length=254)
    number = PhoneNumberField(null=False, blank=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.user

    @receiver(post_save, sender="authentication.RH")
    def addGroup(sender, instance, created, **kwargs):
        if created:
            if instance.role == "RH":
                User.objects.create_user(username=instance.user, role=instance.role, email=instance.email, password=instance.password)

    @receiver(pre_delete, sender="authentication.RH")
    def delete_user(sender, instance, **kwargs):
       
            if User.objects.filter(username=instance.user, role=instance.role).exists():
                user = User.objects.get(username=instance.user, role=instance.role)
                user.delete()
