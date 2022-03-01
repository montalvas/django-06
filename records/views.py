from django.views.generic import CreateView, UpdateView
from django.views.generic import DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Field, Activity
from django.urls import reverse_lazy


################ CREATE ################

class FieldCreate(LoginRequiredMixin, CreateView):   
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-field')
    
class ActivityCreate(LoginRequiredMixin, CreateView):
    model = Activity
    fields = ['number', 'description', 'points', 'details', 'field']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-activity')
    
################ UPDATE ################

class FieldUpdate(LoginRequiredMixin, UpdateView):
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-field')
    
class ActivityUpdate(LoginRequiredMixin, UpdateView):
    model = Activity
    fields = ['number', 'description', 'points', 'details', 'field']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-activity')
    
################ DELETE ################

class FieldDelete(LoginRequiredMixin, DeleteView):
    model = Field 
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-field')
    
class ActivityDelete(LoginRequiredMixin, DeleteView):
    model = Activity
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-activity')

################ LIST ################

class FieldList(LoginRequiredMixin, ListView):
    model = Field
    template_name = 'records/lists/field.html'
    context_object_name = 'fields'
    
class ActivityList(LoginRequiredMixin, ListView):
    model = Activity
    template_name = 'records/lists/activity.html'
    context_object_name = 'activities'

