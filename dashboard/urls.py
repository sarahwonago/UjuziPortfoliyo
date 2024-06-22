from django.urls import path
from .views import *

app_name = 'dashboard'
urlpatterns=[
    path("add_review/", add_review_view, name="review-add"),
    path("view_review/",view_review_view,name="review-view"),
    path("edit_review/", edit_review_view, name="review-edit"),
    path("add_blog/", add_blog_view, name="blog-add"),
    path("view_blog/",view_blog_view,name="blog-view"),
    path("edit_blog/", edit_blog_view, name="blog-edit"),
    path("add_project/", add_project_view, name="project-add"),
    path("view_project/", view_project_view, name="project-view"),
    path("edit_project/", edit_project_view, name="project-edit"),
    path("add_profession/", add_profession_view, name="profession-add"),
    path("view_profession/", view_proffesion_view, name="profession-view"),
    path("edit_profession/",edit_profession_view, name="profession-edit"),
    path("add_work_experience/", add_work_view, name="work-add"),
    path("view_work_experience/", view_work_view, name="work-view"),
    path("edit_work_experience/", edit_work_view, name="work-edit"),
    path("professional_info_edit/", professional_info_view, name="professional-info-edit"),
    path("socials_edit/", socials_view, name="socials-edit"),
    path("profile_edit/", profile_view, name="profile-edit"),
    path("", dashboard, name="dashboard"),
]