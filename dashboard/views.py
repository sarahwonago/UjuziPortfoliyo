from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from userportfoliyo.forms import *
from accounts.forms import UserModForm
from userportfoliyo.models import UserProfileStatistic, Profile

@login_required
def dashboard(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    user_stat, created = UserProfileStatistic.objects.get_or_create(profile=profile)

    blogss = Blog.objects.filter(profile__user=user)
    blogs = Blog.objects.filter(profile__user=user).count()
    projects = Project.objects.filter(profile__user=user).count()
    comments = 0
    for blog in blogss:
        comment=blog.blog_comment.all().count()
        comments=comments+comment
        comment = 0
    
    context={   
        "blogs":blogs,
        "comments":comments,
        "projects":projects,
        "user_stat": user_stat,
    }
    return render(request, "dashboard/dashboard.html", context)

@login_required
def cvpreview_view(request):
    return render(request, "dashboard/cvpreview.html")


def public_cvpreview_view(request, username):
    user=get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    user_stat, created = UserProfileStatistic.objects.get_or_create(profile=profile)
    user_stat.cv_views += 1
    user_stat.save()

    context={
        "user":user,
    }
    return render(request, "dashboard/cvpreview.html", context)

def forbidden(request):
    return render(request, "dashboard/forbidden.html")

@login_required
def profile_view(request):
    user=request.user
    profile= get_object_or_404(Profile, user=user)
  
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save()
            form.save_m2m()

            return redirect("dashboard:profile-edit")
    else:
        form = ProfileForm(instance=profile)

    context = {
        "form":form,
    }
    return render(request, "dashboard/profile.html", context)

@login_required
def personal_edit_view(request):
    if request.method == 'POST':
        form = UserModForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("dashboard:personal-edit")
    else:
        form = UserModForm(instance=request.user)

    context = {
        "form":form,
    }
    return render(request, "dashboard/personal_edit.html", context)

@login_required
def add_work_view(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work=form.save(commit=False)
            work.profile= request.user.profile
            work.save()
            return redirect("dashboard:work-view")
    else:
        form = WorkExperienceForm()
    context = {
        "form":form,
    }
    return render(request, "dashboard/add_work.html", context)

@login_required
def view_work_view(request):
    user=request.user
    q = request.GET.get("q", "")
    profile= get_object_or_404(Profile, user=user)
    work_list = WorkExperience.objects.filter(Q(role__name__icontains=q)|Q(organization__name__icontains=q)|Q(year__icontains=q), profile=profile)
    context={
        "work_list":work_list,
    }
    return render(request, "dashboard/view_work.html", context)

@login_required
def edit_work_view(request, pk):
    work = get_object_or_404(WorkExperience, id=pk)
    if work.profile.user != request.user:
        return redirect('dashboard:forbidden')
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            return redirect("dashboard:work-view")
    else:
       form = WorkExperienceForm(instance=work)  

    context = {
        "form":form,
    }
    return render(request, "dashboard/edit_work.html", context)

@login_required
def delete_work_view(request, pk):
    work = get_object_or_404(WorkExperience, id=pk)

    if work.profile.user != request.user:
        return redirect('dashboard:forbidden')
    
    if request.method == 'POST':
        work.delete()
        return redirect("dashboard:work-view")
    
    context = {
        "work":work,
    }
    return render(request, "dashboard/delete_work.html", context)

@login_required
def add_profession_view(request):
    if request.method == 'POST':
        form = ProfessionForm(request.POST)
        if form.is_valid():
            profession=form.save(commit=False)
            profession.profile= request.user.profile
            profession.save()
            return redirect("dashboard:profession-view")
    else:
       form = ProfessionForm()     
    context = {
        "form":form,
    }
    return render(request, "dashboard/add_profession.html", context)

@login_required
def view_proffesion_view(request):
    user=request.user
    q = request.GET.get("q", "")
    profile= get_object_or_404(Profile, user=user)
    profession_list = Profession.objects.filter(Q(name__name__icontains=q)|Q(description__icontains=q),profile=profile)
    context={
        "profession_list":profession_list
    }
    return render(request, "dashboard/view_profession.html", context)

@login_required
def edit_profession_view(request, pk):
    profession = get_object_or_404(Profession, id=pk)
    
    if profession.profile.user != request.user:
        return redirect('dashboard:forbidden')
    
    if request.method == 'POST':
        form = ProfessionForm(request.POST, instance=profession)
        if form.is_valid():
            form.save()
            return redirect("dashboard:profession-view")
    else:
       form = ProfessionForm(instance=profession)     
    context = {
        "form":form,
    }
    return render(request, "dashboard/edit_profession.html", context)

@login_required
def delete_profession_view(request, pk):
    profession = get_object_or_404(Profession, id=pk)

    if profession.profile.user != request.user:
        return redirect('dashboard:forbidden')
    
    if request.method == 'POST':
        profession.delete()
        return redirect("dashboard:profession-view")
    
    context = {
        "profession":profession,
    }
    return render(request, "dashboard/delete_profession.html", context)

@login_required
def add_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.profile= request.user.profile
            project.save()
            form.save_m2m()
            return redirect("dashboard:project-view")
    else:
        form = ProjectForm()
    context = {
        "form":form,
    }
 
    return render(request, "dashboard/add_project.html", context)

@login_required
def view_project_view(request):
   
    user=request.user
    q = request.GET.get("q", "")
    profile= get_object_or_404(Profile, user=user)
    project_list = Project.objects.filter(Q(name__icontains=q)|Q(description__icontains=q),profile=profile)

    context={
        "project_list":project_list,
    }
    return render(request, "dashboard/view_project.html", context)

@login_required
def edit_project_view(request, pk):
 
    project = get_object_or_404(Project, id=pk)

    if project.profile.user != request.user:
        return redirect('dashboard:forbidden')
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("dashboard:project-view")
    else:
       form = ProjectForm(instance=project)     
    context = {
        "form":form,
    }
    return render(request, "dashboard/edit_project.html", context)

@login_required
def delete_project_view(request, pk):
    project = get_object_or_404(Project, id=pk)

    if project.profile.user != request.user:
        return redirect('dashboard:forbidden')
    
    if request.method == 'POST':
        project.delete()
        return redirect("dashboard:project-view")
    
    context = {
        "project":project,
    }
    return render(request, "dashboard/delete_project.html", context)

@login_required
def add_blog_view(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.profile= request.user.profile
            blog.save()
            return redirect("dashboard:blog-view")
    else:
        form = BlogForm()
    context = {
        "form":form,
    }
 
    return render(request, "dashboard/add_blog.html", context)

@login_required
def view_blog_view(request):
   
    user=request.user
    q = request.GET.get("q", "")
    profile= get_object_or_404(Profile, user=user)
    blog_list = Blog.objects.filter(Q(title__icontains=q)|Q(body__icontains=q),profile=profile)
  
    context={
        "blog_list":blog_list,
    }
    return render(request, "dashboard/view_blogs.html", context)

@login_required
def edit_blog_view(request, pk):
 
    blog = get_object_or_404(Blog, id=pk)

    if blog.profile.user != request.user:
        return redirect('dashboard:forbidden')
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("dashboard:blog-view")
    else:
       form = BlogForm(instance=blog)     
    context = {
        "form":form,
    }
    return render(request, "dashboard/edit_blog.html", context)

@login_required
def delete_blog_view(request, pk):
    blog = get_object_or_404(Blog, id=pk)

    if blog.profile.user != request.user:
        return redirect('dashboard:forbidden')

    if request.method == 'POST':
        blog.delete()
        return redirect("dashboard:blog-view")
    
    context = {
        "blog":blog,
    }
    return render(request, "dashboard/delete_blog.html", context)

@login_required
def add_review_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.profile= request.user.profile
            review.save()
            return redirect("dashboard:review-view")
    else:
       form = ReviewForm()     
    context = {
        "form":form,
    }
    return render(request, "dashboard/add_review.html", context)

@login_required
def view_review_view(request):
    user=request.user
    q = request.GET.get("q", "")
    profile= get_object_or_404(Profile, user=user)
    review_list = Review.objects.filter(Q(reviewer_name__icontains=q)|Q(reviewer_role__name__icontains=q)|Q(reviewer_organization__name__icontains=q),profile=profile)

    context={
        "review_list":review_list
    }
    return render(request, "dashboard/view_review.html", context)

@login_required
def edit_review_view(request, pk):
    review = get_object_or_404(Review, id=pk)

    if review.profile.user != request.user:
        return redirect('dashboard:forbidden')

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("dashboard:review-view")
    else:
       form = ReviewForm(instance=review)     
    context = {
        "form":form,
    }
    return render(request, "dashboard/edit_review.html", context)

@login_required
def delete_review_view(request, pk):
    review = get_object_or_404(Review, id=pk)

    if review.profile.user != request.user:
        return redirect('dashboard:forbidden')

    if request.method == 'POST':
        review.delete()
        return redirect("dashboard:review-view")
    
    context = {
        "review":review,
    }
    return render(request, "dashboard/delete_review.html", context)

@login_required
def add_tech_view(request):
    if request.method == 'POST':
        form = TechnologyForm(request.POST)
        if form.is_valid():
            tech=form.save(commit=False)
            tech.profile= request.user.profile
            tech.save()
            return redirect("dashboard:tech-view")
    else:
        form = TechnologyForm()
    context = {
        "form":form,
    }
    return render(request, "dashboard/add_tech.html", context)

@login_required
def view_tech_view(request):
    user=request.user
    profile= get_object_or_404(Profile, user=user)
    tech_list = Techonology.objects.filter(profile=profile)
    context={
        "tech_list":tech_list,
    }
    return render(request, "dashboard/view_tech.html", context)

@login_required
def edit_tech_view(request, pk):
    tech = get_object_or_404(WorkExperience, id=pk)
    if request.method == 'POST':
        form = TechnologyForm(request.POST, instance=tech)
        if form.is_valid():
            form.save()
            return redirect("dashboard:tech-view")
    else:
       form = TechnologyForm(instance=tech)  

    context = {
        "form":form,
    }
    return render(request, "dashboard/edit_tech.html", context)

@login_required
def delete_tech_view(request, pk):
    tech = get_object_or_404(Techonology, id=pk)
    if request.method == 'POST':
        tech.delete()
        return redirect("dashboard:tech-view")
    
    context = {
        "tech":tech,
    }
    return render(request, "dashboard/delete_tech.html", context)

@login_required
def service_review_view(request):
    if request.method == 'POST':
        form = ServiceReviewForm(request.POST)
        if form.is_valid():
            service=form.save(commit=False)
            service.user= request.user
            service.save()
            return redirect("dashboard:dashboard")
    else:
        form = ServiceReviewForm()
    context = {
        "form":form,
    }
 
    return render(request, "dashboard/service_review.html", context)

@login_required
def add_education_view(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education=form.save(commit=False)
            education.profile= request.user.profile
            education.save()
            return redirect("dashboard:education-view")
    else:
       form = EducationForm()     
    context = {
        "form":form,
    }
    return render(request, "dashboard/add_education.html", context)

@login_required
def view_education_view(request):
    user=request.user
    q = request.GET.get("q", "")
    profile= get_object_or_404(Profile, user=user)
    education_list = Education.objects.filter(Q(field_of_study__name__icontains=q),profile=profile)

    context={
        "education_list":education_list
    }
    return render(request, "dashboard/view_education.html", context)

@login_required
def edit_education_view(request, pk):
    education = get_object_or_404(Education, id=pk)

    if education.profile.user != request.user:
        return redirect('dashboard:forbidden')

    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect("dashboard:education-view")
    else:
       form = EducationForm(instance=education)     
    context = {
        "form":form,
    }
    return render(request, "dashboard/edit_education.html", context)

@login_required
def delete_education_view(request, pk):
    education = get_object_or_404(Education, id=pk)

    if education.profile.user != request.user:
        return redirect('dashboard:forbidden')

    if request.method == 'POST':
        education.delete()
        return redirect("dashboard:education-view")
    
    context = {
        "education":education,
    }
    return render(request, "dashboard/delete_education.html", context)


login_required
def add_certification_view(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            certification=form.save(commit=False)
            certification.profile= request.user.profile
            certification.save()
            return redirect("dashboard:certification-view")
    else:
       form = CertificationForm()     
    context = {
        "form":form,
    }
    return render(request, "dashboard/add_certification.html", context)

@login_required
def view_certification_view(request):
    user=request.user
    q = request.GET.get("q", "")
    profile= get_object_or_404(Profile, user=user)
    certification_list = Certification.objects.filter(Q(name__icontains=q),profile=profile)

    context={
        "certification_list":certification_list
    }
    return render(request, "dashboard/view_certification.html", context)

@login_required
def edit_certification_view(request, pk):
    certification = get_object_or_404(Certification, id=pk)

    if certification.profile.user != request.user:
        return redirect('dashboard:forbidden')

    if request.method == 'POST':
        form = CertificationForm(request.POST, instance=certification)
        if form.is_valid():
            form.save()
            return redirect("dashboard:certification-view")
    else:
       form = CertificationForm(instance=certification)     
    context = {
        "form":form,
    }
    return render(request, "dashboard/edit_certification.html", context)

@login_required
def delete_certification_view(request, pk):
    certification = get_object_or_404(Certification, id=pk)

    if certification.profile.user != request.user:
        return redirect('dashboard:forbidden')

    if request.method == 'POST':
        certification.delete()
        return redirect("dashboard:certification-view")
    
    context = {
        "certification":certification,
    }
    return render(request, "dashboard/delete_certification.html", context)

