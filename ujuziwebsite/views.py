from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
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

def thanks_view(request):
    return render(request, "ujuziwebsite/thanks.html")

def send_email_view(request):
    recipient_email = "zaza@gmail.com"
    subject = request.POST.get("subject", "")
    message = request.POST.get("message", "")
    from_email = request.POST.get("from_email", "")
   
    if subject and message and from_email:
        try:
            send_mail(subject,message,from_email,[recipient_email])

        except BadHeaderError:
            return HttpResponse("Invalid Header found.")
        
        return redirect("ujuziwebsite:thanks")
    else:
        return HttpResponse("Make sure all fields values are entered and are valid.")