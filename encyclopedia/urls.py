from django.urls import path

from . import views

app_name = "articles"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search", views.search, name="search"),
    path("wiki/<slug:title>", views.article, name="article"),
]
