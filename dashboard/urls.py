from django.urls import path
from .views import *

app_name = 'dashboard'
urlpatterns=[
    path("add_tech/", add_tech_view, name="tech-add"),
    path("view_tech/",view_tech_view,name="tech-view"),
    path("edit_tech/<int:pk>", edit_tech_view, name="tech-edit"),
    path("delete_tech/<int:pk>", delete_tech_view, name="tech-delete"),
    path("add_review/", add_review_view, name="review-add"),
    path("view_review/",view_review_view,name="review-view"),
    path("edit_review/<int:pk>", edit_review_view, name="review-edit"),
    path("delete_review/<int:pk>", delete_review_view, name="review-delete"),
    path("add_blog/", add_blog_view, name="blog-add"),
    path("view_blog/",view_blog_view,name="blog-view"),
    path("edit_blog/<int:pk>", edit_blog_view, name="blog-edit"),
    path("delete_blog/<int:pk>", delete_blog_view, name="blog-delete"),
    path("add_project/", add_project_view, name="project-add"),
    path("view_project/", view_project_view, name="project-view"),
    path("edit_project/<int:pk>/", edit_project_view, name="project-edit"),
    path("delete_project/<int:pk>/", delete_project_view, name="project-delete"),
    path("add_profession/", add_profession_view, name="profession-add"),
    path("view_profession/", view_proffesion_view, name="profession-view"),
    path("edit_profession/<int:pk>/",edit_profession_view, name="profession-edit"),
    path("delete_profession/<int:pk>/",delete_profession_view, name="profession-delete"),
    path("add_work_experience/", add_work_view, name="work-add"),
    path("view_work_experience/", view_work_view, name="work-view"),
    path("edit_work_experience/<int:pk>/", edit_work_view, name="work-edit"),
    path("delete_work/<int:pk>/",delete_work_view, name="work-delete"),
    path("personal_info_edit/", personal_edit_view, name="personal-edit"),
    path("service_review/", service_review_view, name="service-review"),
    path("profile_edit/", profile_view, name="profile-edit"),
    path("", dashboard, name="dashboard"),
]