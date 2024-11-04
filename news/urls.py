from django.urls import path
from news.views import index, get_category, get_view_new, add_news

urlpatterns = [
    path(route="", view=index, name="home"),
    path("category/<int:category_id>/", get_category, name="category"),
    path("news/<int:news_id>/", get_view_new, name="view_new"),
    path("news/add_news", add_news, name="add_news")
]
