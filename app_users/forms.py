from django import forms
from django.forms import ModelForm
from .models import Reader, Author, Editor


class ReaderForm(ModelForm):
    class Meta:
        model = Reader
        fields = [
            "username",
            "email",
            "password",
            "name",
            "birth_date",
            "city",
            "state",
            "image",
        ]
        widgets = {"password": forms.PasswordInput()}


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            "username",
            "email",
            "password",
            "name",
            "birth_date",
            "city",
            "state",
            "image",
        ]
        widgets = {"password": forms.PasswordInput()}


class EditorForm(ModelForm):
    class Meta:
        model = Editor
        fields = [
            "username",
            "email",
            "password",
            "name",
            "birth_date",
            "city",
            "state",
            "image",
        ]
        widgets = {"password": forms.PasswordInput()}
