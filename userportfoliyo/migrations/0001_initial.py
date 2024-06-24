# Generated by Django 5.0.6 on 2024-06-24 13:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="blog/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("body", models.TextField()),
            ],
            options={
                "verbose_name": "Blog",
                "verbose_name_plural": "Blogs",
            },
        ),
        migrations.CreateModel(
            name="Institution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=250, unique=True, verbose_name="Institution"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Institution",
                "verbose_name_plural": "Institution",
            },
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=250, unique=True, verbose_name="Organization"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Organization",
                "verbose_name_plural": "Organization",
            },
        ),
        migrations.CreateModel(
            name="SoftSkills",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=250, unique=True, verbose_name="Soft Skills"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Soft Skills",
                "verbose_name_plural": "Soft Skills",
            },
        ),
        migrations.CreateModel(
            name="StudyField",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=250, unique=True, verbose_name="Field of Study"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "StudyField",
                "verbose_name_plural": "StudyField",
            },
        ),
        migrations.CreateModel(
            name="Techonology",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=250, unique=True, verbose_name="Tech-Stack"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Technology",
                "verbose_name_plural": "Technologies",
            },
        ),
        migrations.CreateModel(
            name="TechRole",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=250, unique=True, verbose_name="Tech-Role"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "TechRoles",
                "verbose_name_plural": "TechRole",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment_by", models.CharField(max_length=250)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("comment", models.TextField()),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_comment",
                        to="userportfoliyo.blog",
                    ),
                ),
            ],
            options={
                "verbose_name": "Comments",
                "verbose_name_plural": "Comment",
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "about_me",
                    models.TextField(blank=True, null=True, verbose_name="About"),
                ),
                ("user_cv", models.FileField(blank=True, null=True, upload_to="")),
                ("bio", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("soft_skills", models.ManyToManyField(to="userportfoliyo.softskills")),
                ("tech_stack", models.ManyToManyField(to="userportfoliyo.techonology")),
            ],
            options={
                "verbose_name": "Profile",
                "verbose_name_plural": "Profile",
            },
        ),
        migrations.CreateModel(
            name="Certification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=250, verbose_name="Certification Name"),
                ),
                (
                    "organization",
                    models.CharField(
                        max_length=250, verbose_name="Issuing-Organization"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "description",
                    models.TextField(verbose_name="Summary of Certification"),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile_certifications",
                        to="userportfoliyo.profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Certification",
                "verbose_name_plural": "Certifications",
            },
        ),
        migrations.AddField(
            model_name="blog",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile_blog",
                to="userportfoliyo.profile",
            ),
        ),
        migrations.CreateModel(
            name="ServiceReview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("review", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "ServiceReview",
                "verbose_name_plural": "ServiceReview",
            },
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("graduation_date", models.DateTimeField()),
                ("grade", models.CharField(max_length=250)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("description", models.TextField(verbose_name="Summary of Education")),
                (
                    "institution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userportfoliyo.institution",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile_education",
                        to="userportfoliyo.profile",
                    ),
                ),
                (
                    "field_of_study",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userportfoliyo.studyfield",
                    ),
                ),
            ],
            options={
                "verbose_name": "Education",
                "verbose_name_plural": "Education",
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="project/")),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("demo_link", models.URLField(blank=True, null=True)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile_project",
                        to="userportfoliyo.profile",
                    ),
                ),
                (
                    "technology_used",
                    models.ManyToManyField(to="userportfoliyo.techonology"),
                ),
            ],
            options={
                "verbose_name": "Project",
                "verbose_name_plural": "Projects",
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reviewer_name", models.CharField(max_length=250)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("review", models.TextField()),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile_review",
                        to="userportfoliyo.profile",
                    ),
                ),
                (
                    "reviewer_organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userportfoliyo.organization",
                    ),
                ),
                (
                    "reviewer_role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userportfoliyo.techrole",
                    ),
                ),
            ],
            options={
                "verbose_name": "Review",
                "verbose_name_plural": "Reviews",
            },
        ),
        migrations.CreateModel(
            name="Profession",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("description", models.TextField()),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profession_profile",
                        to="userportfoliyo.profile",
                    ),
                ),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userportfoliyo.techrole",
                    ),
                ),
            ],
            options={
                "verbose_name": "Profession",
                "verbose_name_plural": "Profession",
            },
        ),
        migrations.CreateModel(
            name="WorkExperience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.DateField()),
                ("location", models.CharField(blank=True, max_length=250, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "description",
                    models.TextField(verbose_name="Description of Responsibilities"),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userportfoliyo.organization",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile_workexperience",
                        to="userportfoliyo.profile",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userportfoliyo.techrole",
                    ),
                ),
            ],
            options={
                "verbose_name": "WorkExperience",
                "verbose_name_plural": "WorkExperience",
            },
        ),
    ]
