from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.categories, name='categories'),
    path("category/<category_id>", views.category, name='category'),
    path("add_category/", views.add_category, name='add_category'),
]
