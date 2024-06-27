from django import forms
from datetime import datetime
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio","about_me","tech_stack","soft_skills","user_cv"]
        widgets = {
            "bio":forms.Textarea(attrs={"minlength":100, "maxlength":250})
        }

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ["role","organization","year","description" ]
        widgets = {
            "year": forms.DateInput(attrs={"type":"date","placeholder":"2024-03-04", "max":datetime.now().date()}),
        }

class ProfessionForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = ["name","description"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name","description", "image", "technology_used","github_repo_link","demo_link"]


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title","body", "image"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["reviewer_name","reviewer_role", "reviewer_organization","review"]
     
class TechnologyForm(forms.ModelForm):
 
    class Meta:
        model=Techonology
        fields=["name"]

class ServiceReviewForm(forms.ModelForm):
 
    class Meta:
        model=ServiceReview
        fields=["review"]     

class CommentForm(forms.ModelForm):
 
    class Meta:
        model=Comment
        fields=["comment"] 

class EducationForm(forms.ModelForm):
 
    class Meta:
        model=Education
        fields=["institution","field_of_study","graduation_date", "grade","description"] 
        widgets = {
            "graduation_date": forms.DateInput(attrs={"type":"date","placeholder":"2024-03-04"}),
        }
         

class CertificationForm(forms.ModelForm):
 
    class Meta:
        model=Certification
        fields=["name","organization","description"] 