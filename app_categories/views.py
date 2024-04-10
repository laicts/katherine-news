from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def categories(request):
    return render(request, "categories.html")

def category(request):
    return render(request, "category.html")