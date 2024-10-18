from django.shortcuts import render

from .models import (
    Project,
    Technology
)

def index(request):
    return projects(request)

def projects(request):
    projects = Project.objects.all()
    technologies = Technology.objects.all().order_by('category')
    
    context = {
        'projects': projects,
        'technologies': technologies
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