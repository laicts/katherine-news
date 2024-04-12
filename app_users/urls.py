from django.urls import path
from . import views

urlpatterns = [
    path("", views.users, name='users'),
    path("reader/signup", views.add_reader, name="reader_signup"),
    path("reader/<reader_id>", views.profile_reader, name="reader_profile"),
    path("reader/", views.login_reader, name="reader_login"),
    path("author/signup", views.add_author, name="author_signup"),
    path("author/<author_id>", views.profile_author, name="author_profile"),
    path("author/", views.login_author, name="author_login"),
    path("editor/signup", views.add_editor, name="editor_signup"),
    path("editor/<editor_id>", views.profile_editor, name="editor_profile"),
    path("editor/", views.login_editor, name="editor_login")
    
    
]
