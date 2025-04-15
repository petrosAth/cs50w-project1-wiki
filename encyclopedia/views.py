from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def article(request, title):
    article = util.get_entry(title)
    if article is not None:
        return render(
            request,
            "encyclopedia/article.html",
            {
                "title": title,
                "article": article,
            },
        )
    else:
        return render(
            request,
            "encyclopedia/article.html",
            {"message": "The requested page was not found!"},
        )
