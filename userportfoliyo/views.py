from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa

from .models import *

@login_required
def portfolio_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    techonology = Techonology.objects.filter(profile_technology=profile)
    projects = Project.objects.filter(profile=profile)
    blogs = Blog.objects.filter(profile=profile)
    context = {
        "profile":profile,
        "technology":techonology,
        "projects":projects,
        "blogs":blogs,
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
    
    context = {
        "blog":blog,
    }
    return render(request, "userportfoliyo/blog_detail.html", context)

# @login_required
# def generate_pdf(request):
#     user_profile = Profile.objects.get(user=request.user)
#     template_path = 'userportfoliyo/pdf_template.html'
#     context = {
#         "profile": user_profile
#     }
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
#     template = get_template(template_path)
#     html = template.render(context)
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response