from django.urls import path
from . import views

urlpatterns = [
    path("", views.users, name='users'),
    path("reader", views.add_reader, name="add_reader"),
    path("author", views.add_author, name="add_author"),
    path("editor", views.add_editor, name="add_editor")
]
