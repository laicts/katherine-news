from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from django.http import HttpResponse

from app_categories.models import Category
from app_news.models import News
from .models import Reader, Author, Editor
from .forms import ReaderForm, AuthorForm, EditorForm

from katherine_news.settings import BASE_DIR, STATIC_ROOT, STATIC_URL, STATICFILES_DIRS

# from .forms import UserForm


# Create your views here.





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
    return render(request, 'reader_signup.html', context)

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
    return render(request, 'author_signup.html', context)

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
    return render(request, 'editor_signup.html', context)


def login_reader(request):
    sucess = False
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Reader.objects.filter(username=username, password=password).exists():
            reader = Reader.objects.get(username=username)
            return redirect(f'/users/reader/{reader.id}', foo="bar")
    
    context = {'sucess': sucess}
    return render(request, "reader_login.html", context)

def login_author(request):
    sucess = False
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Author.objects.filter(username=username, password=password).exists():
            author = Author.objects.get(username=username)
            return redirect(f'/users/author/{author.id}', foo="bar")
    
    context = {'sucess': sucess}
    return render(request, "author_login.html", context)

def login_editor(request):
    sucess = False
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Editor.objects.filter(username=username, password=password).exists():
            editor = Editor.objects.get(username=username)
            return redirect(f'/users/editor/{editor.id}', foo="bar")
    
    context = {'sucess': sucess}
    return render(request, "editor_login.html", context)


def profile_reader(request, reader_id):
    reader = Reader.objects.get(id=reader_id)
    return render(request, 'reader_profile.html', {'reader': reader})

def profile_author(request, author_id):
    author = Author.objects.get(id=author_id)
    news_list = News.objects.filter(author_id=author_id)
    return render(request, 'author_profile.html', {'author': author, 'author_news': news_list})

def profile_editor(request, editor_id):
    editor = Editor.objects.get(id=editor_id)
    news_list = News.objects.filter(editor_id=editor_id)
    return render(request, 'editor_profile.html', {'editor': editor, 'editor_news': news_list})