import re
from random import randrange

import markdown
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
                "article": markdown.markdown(article),
            },
        )
    else:
        return render(
            request,
            "encyclopedia/article.html",
            {"message": "The requested page was not found!"},
        )


def search(request):
    query = request.POST["query"]
    articles = util.list_entries()
    found_articles = []
    entries = []

    if articles:
        query_re = re.compile(f".*{re.escape(query)}", re.IGNORECASE)
        found_articles = list(filter(query_re.match, articles))

    if found_articles:
        if query.lower() == found_articles[0].lower():
            title = found_articles[0]
            article = util.get_entry(title)
            return render(
                request,
                "encyclopedia/article.html",
                {"title": title, "article": article},
            )
        else:
            for article in found_articles:
                entries.append(article)
            return render(
                request, "encyclopedia/search-results.html", {"entries": entries}
            )


def random_article(request):
    entries = util.list_entries()
    rng = randrange(1, len(entries))
    title = entries[rng]
    article = util.get_entry(title)
    return render(
        request, "encyclopedia/article.html", {"title": title, "article": article}
    )


def new(request):
    if "title" and "content" not in request.POST:
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST["title"] or "New Article"
        if "edit" not in request.POST and title in util.list_entries():
            return render(
                request,
                "encyclopedia/article.html",
                {"message": "An article with the same title already exists!"},
            )
        content = request.POST["content"] or ""
        util.save_entry(title, content)
        return article(request, title)


def edit(request, title):
    article = util.get_entry(title)
    return render(
        request, "encyclopedia/edit.html", {"title": title, "content": article}
    )
