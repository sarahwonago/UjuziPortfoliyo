from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    #Admin
    path("admin/", admin.site.urls),

    #auth
    path("accounts/", include('django.contrib.auth.urls')),
    
    #Custom
    path("userportfolio/", include('userportfoliyo.urls')),
    path("dashboard/", include('dashboard.urls')),
    path("reg/", include('accounts.urls')),
    path("", LoginView.as_view()),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
