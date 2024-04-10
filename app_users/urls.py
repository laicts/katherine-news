from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_register, name='users'),
    path('signin', views.user_login, name='user_login'),
    path('signup', views.user_register, name='user_register')
]
