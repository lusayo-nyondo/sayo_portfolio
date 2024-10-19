from django.shortcuts import render
from wagtail.urls import views

def index(request):
    return views.serve(
        request,
        '/'        
    )