from django.shortcuts import render
from django.views.generic import TemplateView

class MainViewMainView(TemplateView):
    template_name = "index.html"
