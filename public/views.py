from django.shortcuts import render

def index(request):
    context = {}
    
    return render(
        request,
        'public/pages/index.html',
        context
    )
    
def contact(request):
    context = {}

    return render(
        request,
        'public/pages/contact.html',
        context
    )


def projects(request):
    context = {}
    
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