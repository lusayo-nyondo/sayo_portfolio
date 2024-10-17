from django.shortcuts import render

def index(request):
    context = {}
    
    return render(
        request,
        'services/pages/index.html',
        context
    )
