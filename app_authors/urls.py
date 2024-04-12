from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.authors, name='authors'),
    path("author/post_news", views.post_news, name='post_news'),
    path("author/<author_id>", views.author, name='author'),
]
