from django.urls import path
from .views import *

app_name = "ujuziwebsite"

urlpatterns =[
    path("contact-us/thanks", thanks_view, name="thanks"),
    path("contact-us/thanks", send_email_view, name="send-email"),
    path("contact-us/", contact_view, name="contact-us"),
    path("about/", about_view, name="about"),
    path("", home_view, name="home"),
]