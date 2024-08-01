from django.contrib.auth.models import AbstractUser
from django.db import models
from cities_light.models import Country, Region, SubRegion

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    state = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    lga = models.ForeignKey(SubRegion, on_delete=models.SET_NULL, null=True, blank=True)
    street_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    social_security_number = models.CharField(max_length=11, blank=True, null=True)
    nim_number = models.CharField(max_length=11, blank=True, null=True)
    bvn_number = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
