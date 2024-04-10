from django.shortcuts import render
from django.http import HttpResponse
from .models import Reader, Author, Editor

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


def user_register(request):
    # print(STATICFILES_DIR)
    sucess = False

    if request.method == "GET":
        return render(request, "signup.html")
    
    elif request.method == "POST":
        options = request.POST.get('options')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        name = request.POST.get('name')
        birth_date = request.POST.get('birth_date')
        city = request.POST.get('city')
        state = request.POST.get('state')

        reader = Reader(
            username = username,
            password = password,
            email = email,
            name = name,
            birth_date = birth_date,
            city = city,
            state = state
        )

        print(reader)


        
        # if form.is_valid():
        #     form.save()
        #     sucess = True

    context = {"sucess": sucess}

    return render(request, "signup.html", context)
