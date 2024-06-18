from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Techonology(models.Model):
    class Meta:
        verbose_name_plural = "Technologies"
        verbose_name = "Technology"

    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class Profile(models.Model):

    class Meta:
        verbose_name_plural = "Profile"
        verbose_name = "Profile"
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(blank=True, null=True)
    video_intro = models.FileField(upload_to='video_intros/', null=True, blank=True)
    user_cv =models.FileField(null=True, blank=True)
    profilephoto = models.ImageField(upload_to="profilephoto/", default="profilephoto/profile.png")
    profession = models.CharField(max_length=250)
    bio = models.TextField()
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    fb_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    x_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    techonology = models.ManyToManyField(Techonology)

    def __str__(self):
        return f'{self.user.username}'
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
