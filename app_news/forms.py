from django import forms
from django.forms import ModelForm
from .models import News, Author, Editor


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = [
            "title",
            "subtitle",
            "content",
            "name",
            "birth_date",
            "city",
            "state",
            "image",
        ]
        widgets = {"password": forms.PasswordInput()}

