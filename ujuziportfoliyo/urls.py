from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Admin
    path("admin/", admin.site.urls),

    #Custom
    path("accounts/", include('accounts.urls')),
    path("", include('ujuziwebsite.urls')),
    path("dashboard/", include('userdashboard.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
