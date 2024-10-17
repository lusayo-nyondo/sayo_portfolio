from django.shortcuts import render

from .models import (
    Project
)

def index(request):
    return projects(request)

def projects(request):
    projects = Project.objects.all()
    
    context = {
        'projects': projects
    }
    
    return render(
        request,
        'portfolio/pages/projects.html',
        context
    )
    
def designs(request):
    context = {}
    
    return render(
        request,
        'portfolio/pages/designs.html',
        context
    )
    

def content(request):
    context = {}
    
    return render(
        request,
        'portfolio/pages/designs.html',
        context
    )
    
def services(request):
    context = {}
    
    return render(
        request,
        'portfolio/pages/services.html',
        context
    )