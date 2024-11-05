from django.shortcuts import render, get_object_or_404, redirect

from news.forms import NewsForm
from news.models import News, Category

def index(request):
    news = News.objects.all()
    return render(
        request,
        "news/index.html",
        {
            "news": news,
            "title": "Список новостей",
        }
    )

def get_category(request, category_id: int):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    return render(
        request,
        "news/category.html",
        {
            "news": news,
            "category": category,
        }
    )

def get_view_new(request, news_id: int):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(
        request,
        "news/view_new.html",
        {
            "news_item": news_item
        }
    )

def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            print(">>> save news", news)
            return redirect(news)
    else:
        form = NewsForm()

    return render(
        request,
        "news/add_news.html",
        {"form": form}
    )