from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import *

def user_portfolio(request, username):
    username = request.GET.get("username")
    print(username)
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    profession = Profession.objects.filter(profile=profile)
    projects = Project.objects.filter(profile=profile)
    blogs = Blog.objects.filter(profile=profile)
    reviews = Review.objects.filter(profile=profile)
    
    context = {
        "user":user,
        "profile":profile,
        "projects":projects,
        "blogs":blogs,
        "profession":profession,
        "reviews":reviews,
    }
    return render(request, 'userportfoliyo/public_portfolio.html', context)

@login_required
def portfolio_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    profession = Profession.objects.filter(profile=profile)
    projects = Project.objects.filter(profile=profile)
    blogs = Blog.objects.filter(profile=profile)
    reviews = Review.objects.filter(profile=profile)
    context = {
        "profile":profile,
        "projects":projects,
        "blogs":blogs,
        "profession":profession,
        "reviews":reviews,
    }
    return render(request, "userportfoliyo/portfolio.html", context)

@login_required
def project_detail_view(request, pk):
    project = get_object_or_404(Project, id=pk)
    
    context = {
        "project":project,
    }
    return render(request, "userportfoliyo/project.html", context)

@login_required
def blog_detail_view(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    comments = Comment.objects.filter(blog=blog)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.comment_by = request.user
            comment.blog = blog
            comment.save()
            return redirect("userportfoliyo:portfolio")
    
    else:
        form = CommentForm()

    context = {
        "blog":blog,
        "comments":comments,
        "form":form,
    }
    return render(request, "userportfoliyo/blog_detail.html", context)


def generate_pdf(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = Profile.objects.get(user=user)
    profession = Profession.objects.filter(profile=user_profile).first()
  
    template_path = 'userportfoliyo/pdf_template.html'
    context = {
        "profile": user_profile,
        "profession":profession,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response