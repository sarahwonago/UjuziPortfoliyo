from django import forms
from datetime import datetime
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio","about_me","tech_stack","soft_skills"]
        widgets = {
            "bio":forms.Textarea(attrs={"minlength":100, "maxlength":250}),
            # 'title': forms.TextInput(attrs={'minlength': 5, 'maxlength': 100, 'required': True}),
            # 'body': forms.Textarea(attrs={'required': True}),
            # 'image': forms.FileInput(attrs={'required': True}),
            "tech_stack": forms.CheckboxSelectMultiple(),
            "soft_skills": forms.CheckboxSelectMultiple(),
        }

    new_technology = forms.CharField(label='Add Technology if not exist', required=False)
    new_softskill = forms.CharField(label='Add Soft Skill if not exist', required=False)

    def clean_new_technology(self):
        new_tech = self.cleaned_data.get('new_technology')
        if new_tech:
            # Check if the technology already exists
            existing_tech = Techonology.objects.filter(name__iexact=new_tech).first()
            if existing_tech:
                return existing_tech
            # Create a new technology if it doesn't exist
            else:
                return Techonology.objects.create(name=new_tech)
        return None


    
    def clean_new_softskill(self):
        new_softskill = self.cleaned_data.get('new_softskill')
        if new_softskill:
            # Check if the technology already exists
            existing_tech = SoftSkills.objects.filter(name__iexact=new_softskill).first()
            if existing_tech:
                return existing_tech
            # Create a new technology if it doesn't exist
            else:
                return SoftSkills.objects.create(name=new_softskill)
        return None

    def save(self, commit=True):
        instance = super().save(commit=False)
        new_tech = self.cleaned_data.get('new_technology')
        new_softskill = self.cleaned_data.get('new_softskill')
        if new_tech:
            instance.tech_stack.add(new_tech)
        if new_softskill:
            instance.soft_skills.add(new_softskill)
        if commit:
            instance.save()
        return instance
   
class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ["role","organization","year","description" ]
        widgets = {
            "year": forms.DateInput(attrs={"type":"date","placeholder":"2024-03-04", "max":datetime.now().date()}),
            "role": forms.Select(),
        }

class ProfessionForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = ["name","description"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name","description", "image", "technology_used","github_repo_link","demo_link"]
        widgets= {
            "technology_used":forms.CheckboxSelectMultiple(),
        }


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