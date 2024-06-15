from django.shortcuts import render


def home_view(request):
    return render(request, "ujuziwebsite/index.html")

def about_view(request):
    return render(request, "ujuziwebsite/about.html")

def contact_view(request):
    return render(request, "ujuziwebsite/contact.html")