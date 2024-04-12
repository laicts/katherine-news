from django.shortcuts import render
from app_users.models import Author
from app_news.models import News
from app_news.forms import NewsForm

# Create your views here.
def authors(request):
    return render(request, 'authors.html', {'authors': Author.objects.all()})

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    news_list = News.objects.filter(author_id=author_id)
    return render(request, "author.html", {'author': author, 'author_news':news_list})

def post_news(request):
    sucess = False 
    form = NewsForm(request.POST, request.FILES)
    if form.is_valid(): 
        sucess = True
        form.save()
        # return render(request, 'add_category.html', {'categories': Category.objects.all()})
    context = {
        'form': form,
        'sucesso': sucess
    }
    return render(request, "post_news.html", context)