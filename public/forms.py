from django import forms

from .models import (
    ContactMessage
)

from .widgets import (
    Input,
    TextArea
)

class ContactMessageForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=Input()
    )
    
    email = forms.EmailField(
        widget=Input(),
    )
    
    subject = forms.CharField(
        max_length=255,
        widget=Input()
    )
    
    message = forms.CharField(
        widget=TextArea()
    )
    
    class Meta:
        model = ContactMessage
        
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]