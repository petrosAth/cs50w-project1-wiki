from django.urls import path

from . import views

app_name = "articles"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/new", views.new, name="new"),
    path("wiki/random", views.random_article, name="random_article"),
    path("wiki/search", views.search, name="search"),
    path("wiki/<slug:title>", views.article, name="article"),
]
