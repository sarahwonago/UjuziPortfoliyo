from django.shortcuts import render, get_object_or_404, redirect
from userportfoliyo.forms import *

def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def profile_view(request):
    user=request.user
    profile= get_object_or_404(Profile, user=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dashboard:dashboard")
    else:
        form = ProfileForm(instance=profile)

    context = {
        "form":form,
    }
    return render(request, "dashboard/profile.html", context)


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


def view_work_view(request):
    user=request.user
    profile= get_object_or_404(Profile, user=user)
    work_list = WorkExperience.objects.filter(profile=profile)
    context={
        "work_list":work_list,
    }
    return render(request, "dashboard/view_work.html", context)


def edit_work_view(request, pk):
    work = get_object_or_404(WorkExperience, id=pk)
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

def delete_work_view(request, pk):
    work = get_object_or_404(WorkExperience, id=pk)
    if request.method == 'POST':
        work.delete()
        return redirect("dashboard:work-view")
    
    context = {
        "work":work,
    }
    return render(request, "dashboard/delete_work.html", context)

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

def view_proffesion_view(request):
    user=request.user
    profile= get_object_or_404(Profile, user=user)
    profession_list = Profession.objects.filter(profile=profile)
    context={
        "profession_list":profession_list
    }
    return render(request, "dashboard/view_profession.html", context)


def edit_profession_view(request, pk):
    profession = get_object_or_404(Profession, id=pk)
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

def delete_profession_view(request, pk):
    profession = get_object_or_404(Profession, id=pk)
    if request.method == 'POST':
        profession.delete()
        return redirect("dashboard:profession-view")
    
    context = {
        "profession":profession,
    }
    return render(request, "dashboard/delete_profession.html", context)

def add_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.profile= request.user.profile
            project.save()
            return redirect("dashboard:project-view")
    else:
        form = ProjectForm()
    context = {
        "form":form,
    }
 
    return render(request, "dashboard/add_project.html", context)

def view_project_view(request):
   
    user=request.user
    profile= get_object_or_404(Profile, user=user)
    project_list = Project.objects.filter(profile=profile)
    context={
        "project_list":project_list,
    }
    return render(request, "dashboard/view_project.html", context)


def edit_project_view(request, pk):
 
    project = get_object_or_404(Project, id=pk)
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

def delete_project_view(request, pk):
    project = get_object_or_404(Project, id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect("dashboard:project-view")
    
    context = {
        "project":project,
    }
    return render(request, "dashboard/delete_project.html", context)

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

def view_blog_view(request):
   
    user=request.user
    profile= get_object_or_404(Profile, user=user)
    blog_list = Blog.objects.filter(profile=profile)
    context={
        "blog_list":blog_list,
    }
    return render(request, "dashboard/view_blogs.html", context)


def edit_blog_view(request, pk):
 
    blog = get_object_or_404(Blog, id=pk)
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

def delete_blog_view(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect("dashboard:blog-view")
    
    context = {
        "blog":blog,
    }
    return render(request, "dashboard/delete_blog.html", context)


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

def view_review_view(request):
    user=request.user
    profile= get_object_or_404(Profile, user=user)
    review_list = Review.objects.filter(profile=profile)
    context={
        "review_list":review_list
    }
    return render(request, "dashboard/view_review.html", context)


def edit_review_view(request, pk):
    review = get_object_or_404(Review, id=pk)
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

def delete_review_view(request, pk):
    review = get_object_or_404(Review, id=pk)
    if request.method == 'POST':
        review.delete()
        return redirect("dashboard:review-view")
    
    context = {
        "review":review,
    }
    return render(request, "dashboard/delete_review.html", context)

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


def view_tech_view(request):
    user=request.user
    profile= get_object_or_404(Profile, user=user)
    tech_list = Techonology.objects.filter(profile=profile)
    context={
        "tech_list":tech_list,
    }
    return render(request, "dashboard/view_tech.html", context)


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

def delete_tech_view(request, pk):
    tech = get_object_or_404(Techonology, id=pk)
    if request.method == 'POST':
        tech.delete()
        return redirect("dashboard:tech-view")
    
    context = {
        "tech":tech,
    }
    return render(request, "dashboard/delete_tech.html", context)

