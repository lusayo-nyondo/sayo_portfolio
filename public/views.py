from django.shortcuts import (
    render,
    redirect
)

from django.urls import (
    reverse
)

from django.views.generic import (
    ListView
)

from .forms import (
    ContactMessageForm
)


def index(request):
    tech_stack = tuple()
    
    context = {
        tech_stack: tech_stack
    }
    
    return render(
        request,
        'public/pages/index.html',
        context
    )
    
def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse('public:contact')
            )
    else:
        form = ContactMessageForm()
    
    context = {
        'form': form
    }
    
    return render(
        request,
        'public/pages/contact.html',
        context
    )
