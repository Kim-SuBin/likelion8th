from django.shortcuts import render

# Create your views here.
from django.views.defaults import page_not_found

def handler404(request, exception):
    return page_not_found(request, exception, template_name="404.html")