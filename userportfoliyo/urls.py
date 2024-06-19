from django.urls import path
from .views import *

app_name ="userportfoliyo"

urlpatterns = [
    #path("download_cv", generate_pdf, name="download_cv"),
    path("blog-detail/<int:pk>/", blog_detail_view, name="blog_detail"),
    path("project-detail/<int:pk>/", project_detail_view, name="project_detail"),
    path("", portfolio_view, name="portfolio"),
]