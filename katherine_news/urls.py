
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from app_users.views import home, about
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("about/", about),
    path("users/", include("app_users.urls")),
    path("", include("app_authors.urls")),
    path("", include("app_categories.urls")),
    path("news/", include("app_news.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
