from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import send_mail, BadHeaderError
from xhtml2pdf import pisa

from .models import *

def public_user_portfolio(request, username):
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

@login_required
def generate_pdf(request):
    user_profile = get_object_or_404(Profile, user=request.user)
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