from django.views.generic import CreateView, UpdateView
from django.views.generic import DeleteView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404

from .models import Field, Activity, Official, State, City, Campus, Status, Validation
from .models import Situation, Grade, Progression, Receipt

from django.urls import reverse_lazy


################ CREATE ################

class FieldCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-field')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cadastrar Campo Novo'
        
        return context
    
    
class ActivityCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Activity
    fields = ['number', 'description', 'points', 'details', 'field']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-activity')
    
class StateCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = State
    fields = ['name', 'uf']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-state')
    
class CityCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = City
    fields = ['name', 'state']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-city')
    
class CampusCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Campus
    fields = ['name', 'city', 'address', 'phone']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-campus')
    
class OfficialCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Official
    fields = ['full_name', 'siape', 'cpf', 'campus']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-official')
    
class StatusCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Status
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-status')

class SituationCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Situation
    fields = ['status', 'details']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-situation')
    
class GradeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Grade
    fields = ['name', 'level', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-grade')
    
class ProgressionCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Progression
    fields = ['grade', 'initial_date', 'final_date', 'observation']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-progression')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)
    
class ReceiptCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Receipt
    fields = ['progression', 'activity', 'quantity', 'initial_date', 'final_date', 'file']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-progression')
    
class ValidationCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Validation
    fields = ['quantity', 'justification']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-progression')
    

################ UPDATE ################


class FieldUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-field')
    
class ActivityUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Activity
    fields = ['number', 'description', 'points', 'details', 'field']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-activity')
    
class StateUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = State
    fields = ['name', 'uf']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-state')
    
class CityUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = City
    fields = ['name', 'state']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-city')
    
class CampusUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Campus
    fields = ['name', 'city', 'address', 'phone']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-campus')
    
class OfficialUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Official
    fields = ['full_name', 'siape', 'cpf', 'campus']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-official')
    
class StatusUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Status
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-status')

class SituationUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Situation
    fields = ['status', 'details']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-situation')
    
class GradeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Grade
    fields = ['name', 'level', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-grade')
    
class ProgressionUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Progression
    fields = ['grade', 'initial_date', 'final_date', 'observation']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-progression')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Progression,
                                        pk=self.kwargs['pk'],
                                        user=self.request.user
                                        )
        return self.object
    
class ReceiptUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Receipt
    fields = ['progression', 'activity', 'quantity', 'initial_date', 'final_date', 'file']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-progression')
    
class ValidationUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Validation
    fields = ['quantity', 'justification']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-progression')
    

################ DELETE ################


class FieldDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
    model = Field 
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-field')
    
class ActivityDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
    model = Activity
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-activity')
    
class StateDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
    model = State
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-state')
    
class CityDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
    model = City
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-city')
    
class CampusDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
    model = Campus
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-campus')
    
class OfficialDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
    model = Official
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-official')
    
class StatusDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
    model = Status
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-status')

class SituationDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
    model = Situation
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-situation')
    
class GradeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
    model = Grade
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-grade')
    
class ProgressionDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
    model = Progression
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-progression')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Progression,
                                        pk=self.kwargs['pk'],
                                        user=self.request.user
                                        )
        return self.object
        
    
class ReceiptDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
    model = Receipt
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-progression')
    
class ValidationDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador" 
    model = Validation
    template_name = 'records/form-delete.html'
    success_url = reverse_lazy('records:list-progression')


################ LIST ################


class FieldList(LoginRequiredMixin, ListView):
    model = Field
    template_name = 'records/lists/field.html'
    context_object_name = 'fields'
    
class ActivityList(LoginRequiredMixin, ListView):
    model = Activity
    template_name = 'records/lists/activity.html'
    context_object_name = 'activities'
    
class StateList(LoginRequiredMixin, ListView):
    model = State
    template_name = 'records/lists/state.html'
    context_object_name = 'states'
    
class CityList(LoginRequiredMixin, ListView): 
    model = City
    template_name = 'records/lists/city.html'
    context_object_name = 'cities'
    
class CampusList(LoginRequiredMixin, ListView): 
    model = Campus
    template_name = 'records/lists/campus.html'
    context_object_name = 'campus'
    
class OfficialList(LoginRequiredMixin, ListView): 
    model = Campus
    template_name = 'records/lists/official.html'
    context_object_name = 'officials'
    
class StatusList(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'records/lists/status.html'
    context_object_name = 'status'

class SituationList(LoginRequiredMixin, ListView):
    model = Situation
    template_name = 'records/lists/situation.html'
    context_object_name = 'situations'
    
class GradeList(LoginRequiredMixin, ListView):
    model = Grade
    template_name = 'records/lists/grade.html'
    context_object_name = 'grades'
    
class ProgressionList(LoginRequiredMixin, ListView):
    model = Progression
    template_name = 'records/lists/progression.html'
    context_object_name = 'progressions'
    
    def get_queryset(self):
        self.object_list = Progression.objects.filter(user=self.request.user)
        return self.object_list
    
class ReceiptList(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = 'records/lists/receipt.html'
    context_object_name = 'receipts'
    
class ValidationList(LoginRequiredMixin, ListView):
    model = Validation
    template_name = 'records/lists/validation.html'
    context_object_name = 'validations'

