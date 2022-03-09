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
        context["title"] = 'Cadastrar Campo'
        context['link'] = "records:list-field"
        
        return context
    
    
class ActivityCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Activity
    fields = ['number', 'description', 'points', 'details', 'field']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-activity')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cadastrar Atividade'
        context['link'] = "records:list-activity"
        
        return context
    
class StateCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = State
    fields = ['name', 'uf']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-state')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cadastrar Estado'
        context['link'] = "records:list-state"
        
        return context
    
class CityCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = City
    fields = ['name', 'state']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-city')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cadastrar Cidade'
        context['link'] = "records:list-city"
        
        return context
    
class CampusCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Campus
    fields = ['name', 'city', 'address', 'phone']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-campus')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cadastrar Campus'
        context['link'] = "records:list-campus"
        
        return context
    
class OfficialCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Official
    fields = ['full_name', 'siape', 'cpf', 'campus']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-official')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cadastrar Servidor'
        context['link'] = "records:list-official"
        
        return context
    
class StatusCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Status
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-status')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cadastrar Status'
        context['link'] = "records:list-status"
        
        return context

class SituationCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Situation
    fields = ['status', 'details']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-situation')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cadastrar Situação'
        context['link'] = "records:list-situation"
        
        return context
    
class GradeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Grade
    fields = ['name', 'level', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-grade')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cadastrar Classe'
        context['link'] = "records:list-grade"
        
        return context
    
class ProgressionCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Progression
    fields = ['grade', 'initial_date', 'final_date', 'observation']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-progression')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cadastrar Progressão'
        context['link'] = "records:list-progression"
        
        return context
    
class ReceiptCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Receipt
    fields = ['progression', 'activity', 'quantity', 'initial_date', 'final_date', 'file']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-receipt')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cadastrar Recibo'
        context['link'] = "records:list-receipt"
        
        return context
    
class ValidationCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador" 
    model = Validation
    fields = ['quantity', 'justification']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-progression')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cadastrar Validação'
        context['link'] = "records:list-validation"
        
        return context
    
################ UPDATE ################


class FieldUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Field
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-field')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Atualizar Campo'
        context['link'] = "records:list-field"
        
        return context
    
class ActivityUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Activity
    fields = ['number', 'description', 'points', 'details', 'field']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-activity')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Atualizar Atividade'
        context['link'] = "records:list-activity"
        
        return context
    
class StateUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = State
    fields = ['name', 'uf']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-state')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Atualizar Estado'
        context['link'] = "records:list-state"
        
        return context
    
class CityUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = City
    fields = ['name', 'state']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-city')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Atualizar Cidade'
        context['link'] = "records:list-city"
        
        return context
    
class CampusUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Campus
    fields = ['name', 'city', 'address', 'phone']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-campus')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Atualizar Campus'
        context['link'] = "records:list-campus"
        
        return context
    
class OfficialUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Official
    fields = ['full_name', 'siape', 'cpf', 'campus']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-official')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Atualizar Servidor'
        context['link'] = "records:list-official"
        
        return context
    
class StatusUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Status
    fields = ['name', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-status')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Atualizar Status'
        context['link'] = "records:list-status"
        
        return context

class SituationUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Situation
    fields = ['status', 'details']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-situation')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Atualizar Situação'
        context['link'] = "records:list-situation"
        
        return context
    
class GradeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Grade
    fields = ['name', 'level', 'description']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-grade')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Atualizar Classe'
        context['link'] = "records:list-grade"
        
        return context
    
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Atualizar Progressão'
        context['link'] = "records:list-progression"
        
        return context
    
class ReceiptUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Receipt
    fields = ['progression', 'activity', 'quantity', 'initial_date', 'final_date', 'file']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-progression')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Atualizar Recibo'
        context['link'] = "records:list-receipt"
        
        return context
    
class ValidationUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador" 
    model = Validation
    fields = ['quantity', 'justification']
    template_name = 'records/form.html'
    success_url = reverse_lazy('records:list-progression')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Atualizar Validação'
        context['link'] = "records:list-validation"
        
        return context
    

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

