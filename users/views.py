from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User, Group

from .forms import UserForm
from .models import Profile


class UserCreate(CreateView):
    template_name = 'users/register.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('auth:login')
    
    def form_valid(self, form):
        group = get_object_or_404(Group, name='Docente')
        url = super().form_valid(form)
        self.object.groups.add(group)
        
        Profile.objects.create(user=self.object)
        
        return url

class ProfileUpdate(UpdateView):
    template_name = 'records/form.html'
    model = Profile
    fields = ['full_name', 'cpf', 'phone']
    success_url = reverse_lazy('website:index')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Profile, user=self.request.user)
        return self.object
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Atualizar Perfil'
        context['link'] = 'website:index'
        
        return context
