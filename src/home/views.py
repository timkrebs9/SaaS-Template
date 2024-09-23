import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisits

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisits.objects.all()
    qs_page = PageVisits.objects.filter(path=request.path)
    my_title = "Hello there..."
    html_template = "home.html"
    my_context = {
        "page_title": my_title,
        "page_visit_count": qs_page.count(),
        "total_page_visit_count": qs.count(),
    }

    PageVisits.objects.create(path=request.path)
    return render(request, html_template, my_context)