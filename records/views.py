from django.views.generic import CreateView, UpdateView
from django.views.generic import DeleteView, ListView
from .models import Field, Activity
from django.urls import reverse_lazy


################ CREATE ################

class FieldCreate(CreateView):
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-field')
    
class ActivityCreate(CreateView):
    model = Activity
    fields = ['number', 'description', 'points', 'details', 'field']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-activity')
    
################ UPDATE ################

class FieldUpdate(UpdateView):
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-field')
    
class ActivityUpdate(UpdateView):
    model = Activity
    fields = ['number', 'description', 'points', 'details', 'field']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-activity')
    
################ DELETE ################

class FieldDelete(DeleteView):
    model = Field 
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-field')
    
class ActivityDelete(DeleteView):
    model = Activity
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-activity')

################ LIST ################

class FieldList(ListView):
    model = Field
    template_name = 'records/lists/field.html'
    context_object_name = 'fields'
    
class ActivityList(ListView):
    model = Activity
    template_name = 'records/lists/activity.html'
    context_object_name = 'activities'

