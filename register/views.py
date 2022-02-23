from dataclasses import fields
from django.views.generic import CreateView
from .models import Field, Activity
from django.urls import reverse_lazy


class FieldCreate(CreateView):
    model = Field
    fields = ['name', 'description']
    template_name = 'register/form.html'
    success_url = reverse_lazy('website:index')
    
class ActivityCreate(CreateView):
    model = Activity
    fields = ['number', 'description', 'points', 'details']
    template_name = 'register/form.html'
    success_url = reverse_lazy('website:index')
