from django.shortcuts import render
from .models import Category
from .forms import CategoryForm


# Create your views here.
def categories(request):
    return render(request, 'categories.html', {'categories': Category.objects.all()})


def category(request, category_id):
    return render(request, "category.html", {'category': Category.objects.get(id=category_id)})


def add_category(request):
    sucess = False 
    form = CategoryForm(request.POST, request.FILES)
    if form.is_valid(): 
        sucess = True
        form.save()
        # return render(request, 'add_category.html', {'categories': Category.objects.all()})
    context = {
        'form': form,
        'sucesso': sucess
    }
    return render(request, 'add_category.html', context)

    
