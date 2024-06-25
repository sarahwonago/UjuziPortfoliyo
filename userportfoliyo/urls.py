from django.urls import path
from .views import *

app_name ="userportfoliyo"

urlpatterns = [
    path("get-in-touch/<str:username>/", public_send_email_view, name="public-send-email"),
    path("download-cv/", generate_pdf, name="download_cv"),
    path("<str:username>/", public_user_portfolio, name='user_portfolio'),
    path("download-cv/<str:username>/", public_generate_pdf, name="public_download_cv"),
    path("blog-detail/<int:pk>/", blog_detail_view, name="blog_detail"),
    path("public/blog-detail/<int:pk>/<str:username>/", public_blog_detail_view, name="public_blog_detail"),
    path("project-detail/<int:pk>/", project_detail_view, name="project_detail"),
    path("public/project-detail/<int:pk>/<str:username>/", public_project_detail_view, name="public_project_detail"),
    path("", portfolio_view, name="portfolio"),
]
