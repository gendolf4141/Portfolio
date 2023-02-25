from django.shortcuts import render
from .models import Project


def home(requests):
    projects = Project.objects.all()
    return render(requests, "my_portfolio/home.html", {'projects': projects})
# Create your views here.
