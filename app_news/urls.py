from django.urls import path
from . import views

urlpatterns = [
    path("news/<news_id>", views.news, name='news'),
]
