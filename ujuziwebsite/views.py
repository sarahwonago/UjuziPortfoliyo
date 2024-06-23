from django.shortcuts import render
from userportfoliyo.models import ServiceReview

def home_view(request):
    reviews = ServiceReview.objects.all()
    context ={
        "reviews":reviews,
    }
    return render(request, "ujuziwebsite/index.html", context)

def about_view(request):
    return render(request, "ujuziwebsite/about.html")

def contact_view(request):
    return render(request, "ujuziwebsite/contact.html")