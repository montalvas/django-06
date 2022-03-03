from django.views.generic import CreateView, UpdateView
from django.views.generic import DeleteView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import Field, Activity

from django.urls import reverse_lazy


################ CREATE ################

class FieldCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-field')
    
class ActivityCreate(GroupRequiredMixin ,LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Activity
    fields = ['number', 'description', 'points', 'details', 'field']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-activity')
    
################ UPDATE ################

class FieldUpdate(GroupRequiredMixin ,LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-field')
    
class ActivityUpdate(GroupRequiredMixin ,LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Activity
    fields = ['number', 'description', 'points', 'details', 'field']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-activity')
    
################ DELETE ################

class FieldDelete(GroupRequiredMixin ,LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
    model = Field 
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-field')
    
class ActivityDelete(GroupRequiredMixin ,LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
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

