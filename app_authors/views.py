from django.shortcuts import render

# Create your views here.
def authors(request):
    return render(request, "authors.html")

def author(request):
    return render(request, "author.html")