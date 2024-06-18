from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Admin
    path("admin/", admin.site.urls),

    #Custom
    path("userportfolio/", include('userportfoliyo.urls')),
    path("dashboard/", include('userdashboard.urls')),
    path("accounts/", include('accounts.urls')),
    path("", include('ujuziwebsite.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
