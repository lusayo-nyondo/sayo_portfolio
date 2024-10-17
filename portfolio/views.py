from django.shortcuts import render, HttpResponse

def index(request):
    """context = {}

    return render(
        request,
        'portfolio/pages/index.html',
        context
    )"""
    return projects(request)

def projects(request):
    context = {
        'projects': tuple()
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