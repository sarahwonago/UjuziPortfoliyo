from django.urls import path
from .views import *

app_name ="userportfoliyo"

urlpatterns = [
    #path("download_cv", generate_pdf, name="download_cv"),
    path("", portfolio_view, name="portfolio"),
]