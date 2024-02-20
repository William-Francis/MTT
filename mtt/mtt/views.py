from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "mtt/index.html"
