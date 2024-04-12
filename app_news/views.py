from django.shortcuts import render

from app_news.models import News


def home(request):
    news_list = News.objects.all()
    emphasis = news_list[0]

    return render(request, "index.html", {'emphasis_news': emphasis, 'column1_news': [news_list[0], news_list[1], news_list[2]], 'column2_news': [news_list[3], news_list[4], news_list[5]]})

def about(request):
    return render(request, "about.html")

def news(request, news_id):
    sucess = False
    if News.objects.filter(id=news_id).exists():
        news = News.objects.get(id=news_id)
        sucess = True

    context = {'sucess': sucess, 'news': news}
    return render(request, "single-post.html", context=context)

def add_news(request):
    return render(request, "add_news.html")
