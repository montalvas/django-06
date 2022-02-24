from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Field, Activity
from django.urls import reverse_lazy


################ CREATE ################

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
    
################ DELETE ################

class FieldDelete(DeleteView):
    model = Field 
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('website:index')
    
class ActivityDelete(DeleteView):
    model = Activity
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('website:index')
