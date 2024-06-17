from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #Admin
    path("admin/", admin.site.urls),

    #Auth app
    path("accounts/", include('django.contrib.auth.urls')),

    #Custom
    path("", include('ujuziwebsite.urls')),
    path("dashboard/", include('userdashboard.urls')),
    path("accounts/", include('accounts.urls')),
]
