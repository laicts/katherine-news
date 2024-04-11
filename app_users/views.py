from django.shortcuts import render
from django.http import HttpResponse
from .models import Reader, Author, Editor
from .forms import ReaderForm, AuthorForm, EditorForm

from katherine_news.settings import BASE_DIR, STATIC_ROOT, STATIC_URL, STATICFILES_DIRS

# from .forms import UserForm


# Create your views here.


def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def user_login(request):
    if request.method == "GET":
        return render(request, "signin.html")

def users(request):
    return render(request, "users.html")

def add_reader(request):
    sucess = False 
    form = ReaderForm(request.POST, request.FILES)
    if form.is_valid(): 
        sucess = True
        form.save()
        # return render(request, 'add_category.html', {'categories': Category.objects.all()})
    context = {
        'form': form,
        'sucesso': sucess
    }
    return render(request, 'users_reader.html', context)

def add_author(request):
    sucess = False 
    form = AuthorForm(request.POST, request.FILES)
    if form.is_valid(): 
        sucess = True
        form.save()
        # return render(request, 'add_category.html', {'categories': Category.objects.all()})
    context = {
        'form': form,
        'sucesso': sucess
    }
    return render(request, 'users_author.html', context)

def add_editor(request):
    sucess = False 
    form = EditorForm(request.POST, request.FILES)
    if form.is_valid(): 
        sucess = True
        form.save()
        # return render(request, 'add_category.html', {'categories': Category.objects.all()})
    context = {
        'form': form,
        'sucesso': sucess
    }
    return render(request, 'users_editor.html', context)
