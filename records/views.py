from django.views.generic import CreateView, UpdateView
from .models import Field, Activity
from django.urls import reverse_lazy


class FieldCreate(CreateView):
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('website:index')
    
class ActivityCreate(CreateView):
    model = Activity
    fields = ['number', 'description', 'points', 'details']
    template_name = 'records/form.html'
    success_url = reverse_lazy('website:index')
    
################ UPDATE ################

class FieldUpdate(UpdateView):
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('website:index')
    
class ActivityUpdate(UpdateView):
    model = Activity
    fields = ['number', 'description', 'points', 'details']
    template_name = 'records/form.html'
    success_url = reverse_lazy('website:index')
