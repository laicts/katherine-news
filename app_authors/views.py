from django.shortcuts import render
from app_users.models import Author
from app_news.models import News

# Create your views here.
def authors(request):
    return render(request, 'authors.html', {'authors': Author.objects.all()})

def author(request, author_id):
    return render(request, "author.html", {'author': Author.objects.get(id=author_id),
                                           'news':News.objects.filter(author_id=author_id)})