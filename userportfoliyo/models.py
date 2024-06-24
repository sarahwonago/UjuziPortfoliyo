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
    
class SoftSkills(models.Model):
    class Meta:
        verbose_name_plural = "Soft Skills"
        verbose_name = "Soft Skills"

    name = models.CharField("Soft Skills",max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Institution(models.Model):
    class Meta:
        verbose_name_plural = "Institution"
        verbose_name = "Institution"

    name = models.CharField("Institution",max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Organization(models.Model):
    class Meta:
        verbose_name_plural = "Organization"
        verbose_name = "Organization"

    name = models.CharField("Organization",max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class StudyField(models.Model):
    class Meta:
        verbose_name_plural = "StudyField"
        verbose_name = "StudyField"

    name = models.CharField("Field of Study",max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class TechRole(models.Model):
    class Meta:
        verbose_name_plural = "TechRole"
        verbose_name = "TechRoles"

    name = models.CharField("Tech-Role",max_length=250, unique=True)
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
    soft_skills = models.ManyToManyField(SoftSkills)

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
    name = models.ForeignKey(TechRole, on_delete=models.CASCADE)
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
    role = models.ForeignKey(TechRole, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    year = models.DateField()
    location = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField("Description of Responsibilities")

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
    reviewer_role =models.ForeignKey(TechRole, on_delete=models.CASCADE)
    reviewer_organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.TextField()

    def __str__(self):
        return self.reviewer_name
    
class ServiceReview(models.Model):
    class Meta:
        verbose_name_plural = "ServiceReview"
        verbose_name = "ServiceReview"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    #rate= models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return self.user.username
    
class Education(models.Model):
    class Meta:
        verbose_name_plural = "Education"
        verbose_name = "Education"

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_education")
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    field_of_study = models.ForeignKey(StudyField, on_delete=models.CASCADE)
    graduation_date = models.DateTimeField()
    grade = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField("Summary of Education")

    def __str__(self):
        return self.institution.name
    
class Certification(models.Model):
    class Meta:
        verbose_name_plural = "Certifications"
        verbose_name = "Certification"

    name= models.CharField("Certification Name",max_length=250)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_certifications")
    organization = models.CharField("Issuing-Organization",max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField("Summary of Certification")

    def __str__(self):
        return self.name