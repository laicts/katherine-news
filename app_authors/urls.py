from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.authors, name='authors'),
    path("author/<author_id>", views.author, name='author'),
]
