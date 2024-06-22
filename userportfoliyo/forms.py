from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name","last_name","email","about_me", "profilephoto", "phone_number","country"]
        widgets = {
            "email": forms.EmailInput(attrs={"placeholder":"Enter Email"}),
            "first_name": forms.TextInput(attrs={"placeholder":"Enter First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder":"Enter Last Name"}),
            "about_me": forms.Textarea(attrs={"placeholder":"A brief about you.."}),
            "phone_number": forms.TextInput(attrs={"placeholder":"Enter Phone Number"}),
            "country": forms.TextInput(attrs={"placeholder":"Kenya/Nairobi"}),
        }
        
class SocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = ["fb_link", "instagram_link", "x_link", "github_link", "linkedin_link"]

class ProfessionalProfileForm(forms.ModelForm):
    class Meta:
        model = ProfessionalProfile
        fields = ["bio","techonology","user_cv" ]

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ["role","organization","year","description" ]
        widgets = {
            "year": forms.DateInput(attrs={"type":"Date","placeholder":"2024-03-04"}),
        }

class ProfessionForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = ["name","description"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name","description", "image", "technology_used","demo_link"]


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title","body", "image"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["reviewer_name","reviewer_role", "reviewer_organization","review"]
     