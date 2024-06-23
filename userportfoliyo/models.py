from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save


User =get_user_model()

class Techonology(models.Model):
    class Meta:
        verbose_name_plural = "Technologies"
        verbose_name = "Technology"

    name = models.CharField("Tech-Stack",max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):

    class Meta:
        verbose_name_plural = "Profile"
        verbose_name = "Profile"
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField("About",blank=True, null=True)
    user_cv =models.FileField(null=True, blank=True)
    bio = models.TextField()
    tech_stack = models.ManyToManyField(Techonology)

    def __str__(self):
        return f'{self.user.username}'
    

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    
class Profession(models.Model):
    class Meta:
        verbose_name_plural = "Profession"
        verbose_name = "Profession"

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profession_profile")
    name = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.name



class WorkExperience(models.Model):

    class Meta:
        verbose_name_plural = "WorkExperience"
        verbose_name = "WorkExperience"

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_workexperience")
    role = models.CharField(max_length=250)
    organization = models.CharField(max_length=250)
    year = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.organization
    
class Project(models.Model):

    class Meta:
        verbose_name_plural = "Projects"
        verbose_name = "Project"

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_project")
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="project/")
    technology_used = models.ManyToManyField(Techonology)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    demo_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    class Meta:
        verbose_name_plural = "Blogs"
        verbose_name = "Blog"

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_blog")
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="blog/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    class Meta:
        verbose_name_plural = "Comment"
        verbose_name = "Comments"

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_comment")
    comment_by = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment_by
    
class Review(models.Model):
    class Meta:
        verbose_name_plural = "Reviews"
        verbose_name = "Review"

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_review")
    reviewer_name = models.CharField(max_length=250)
    reviewer_role = models.CharField(max_length=250)
    reviewer_organization = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.TextField()

    def __str__(self):
        return self.reviewer_name