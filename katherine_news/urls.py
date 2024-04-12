
from django.contrib import admin
from django.urls import path, include
from app_news.views import home, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("about/", about),
    path("users/", include("app_users.urls")),
    path("", include("app_authors.urls")),
    path("", include("app_categories.urls")),
    path("", include("app_news.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
