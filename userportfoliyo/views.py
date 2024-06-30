from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import send_mail, BadHeaderError
from xhtml2pdf import pisa
from weasyprint import HTML

from .models import *

def public_user_portfolio(request, username):
    user = get_object_or_404(User, username=username)
    
    profile = get_object_or_404(Profile, user=user)
    
    if request.user != user:
        user_stat, created = UserProfileStatistic.objects.get_or_create(profile=profile)
        user_stat.profile_views += 1
        user_stat.save()
    
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


def public_blog_detail_view(request, pk, username):
    user = get_object_or_404(User, username=username)
    blog = get_object_or_404(Blog, id=pk, profile__user=user)
    
    comments = Comment.objects.filter(blog=blog)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.comment_by = request.user
            comment.blog = blog
            comment.save()
            return redirect(f'/userportfolio/public/blog-detail/{pk}/{username}/')
    
    else:
        form = CommentForm()

    context = {
        "blog":blog,
        "comments":comments,
        "form":form,
    }
    return render(request, "userportfoliyo/public_blog_detail.html", context)


def public_project_detail_view(request, pk, username):
    user = get_object_or_404(User, username=username)
    project = get_object_or_404(Project, id=pk, profile__user=user)
    
    context = {
        "project":project,
    }
    return render(request, "userportfoliyo/public_project.html", context)

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

def public_generate_pdf(request, username):
    user = get_object_or_404(User, username=username)

    profile = get_object_or_404(Profile, user=user)
    
    if request.user != user:
        user_stat, created = UserProfileStatistic.objects.get_or_create(profile=profile)
        user_stat.cv_downloads += 1
        user_stat.save()
  
    template= get_template('userportfoliyo/pdf_template.html')
    context = {
        "user":user,
    }

    html_content = template.render(context)

    pdf_file = HTML(string=html_content).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{user.username}_profile.pdf"'
    
    return response


@login_required
def generate_pdf(request):
    user = request.user
  
    template= get_template('userportfoliyo/pdf_template.html')

    context = {
        "user":user,
    }
    html_content = template.render(context)

    pdf_file = HTML(string=html_content).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{request.user.username}_profile.pdf"'
    
    return response


def public_send_email_view(request, username):
    user = get_object_or_404(User, username=username)
    user_email = user.email
    subject = request.POST.get("subject", "")
    message = request.POST.get("message", "")
    from_email = request.POST.get("from_email", "")
   
    if not user_email:
        return HttpResponse(f'Sorry, {user.username} has not specified their email.')
    if subject and message and from_email:
        try:
            send_mail(subject,message,from_email,[user_email])

        except BadHeaderError:
            return HttpResponse("Invalid Header found.")
        
        return HttpResponse(f'Thank you. Message sent to {user.username}.')
    else:
        return HttpResponse("Make sure all fields values are entered and are valid.")