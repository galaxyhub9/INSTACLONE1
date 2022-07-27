from django.shortcuts import render
from django.views.generic import CreateView,ListView

from account.models import posts

class indexView(ListView):
    template_name = 'index.html'
    model = posts
    context_object_name = 'recentpost'
    ordering = ['posted_at']
    
    
    