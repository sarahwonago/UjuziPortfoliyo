from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profilephoto = models.ImageField("ProfilePicture",upload_to="profilephoto/", default="profilephoto/profile.png")
    phone_number = models.CharField("Phone Number",max_length=250, null=True, blank=True)
    country = models.CharField("Country/City",max_length=250, null=True, blank=True)
    fb_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    x_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
