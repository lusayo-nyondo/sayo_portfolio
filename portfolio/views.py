from django.shortcuts import render, HttpResponse

def index(request):
    context = {}

    return render(
        request,
        'portfolio/index.html',
        context
    )

def projects(request):
    context = {
        'projects': tuple()
    }
    
    return render(
        request,
        'public/pages/projects.html',
        context
    )
    
def designs(request):
    context = {}
    
    return render(
        request,
        'public/pages/designs.html',
        context
    )
    

def content(request):
    context = {}
    
    return render(
        request,
        'public/pages/designs.html',
        context
    )
    
def services(request):
    context = {}
    
    return render(
        request,
        'public/pages/services.html',
        context
    )