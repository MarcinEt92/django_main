from django.shortcuts import render

from .helpers.episodes import Episodes


# Create your views here.
def index(request):
    return render(request, "base/base.html")


def html_tutorial(request):
    tutorial_name = "html"
    context = {
        "tutorial_name": tutorial_name,
        "episodes": Episodes.get_episodes(tutorial_name)
    }
    return render(request, "base/extended.html", context)


def css_tutorial(request):
    tutorial_name = "css"
    context = {
        "tutorial_name": tutorial_name,
        "episodes": Episodes.get_episodes(tutorial_name)
    }
    return render(request, "base/extended.html", context)


def js_tutorial(request):
    tutorial_name = "js"
    context = {
        "tutorial_name": tutorial_name,
        "episodes": Episodes.get_episodes(tutorial_name)
    }
    return render(request, "base/extended.html", context)


def tutorial_generic(request, tutorial_name, tutorial_id):
    context = {
        "tutorial_name": tutorial_name,
        "tutorial_id": tutorial_id,
        "episodes": Episodes.get_episodes(tutorial_name)
    }
    return render(request, "base/frame.html", context)


def frames(request, tutorial_name, tutorial_id):
    template_paths = {
        "html": f"html/html_{tutorial_id}.html",
        "css": f"css/css_{tutorial_id}.html",
        "js": f"js/js_{tutorial_id}.html",
    }
    template_name = template_paths.get(tutorial_name)
    return render(request, template_name)
