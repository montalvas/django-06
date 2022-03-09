from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from django.views.generic import CreateView
from django.contrib.auth.models import User, Group

from .forms import UserForm


class UserCreate(CreateView):
    template_name = 'users/register.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('auth:login')
    
    def form_valid(self, form):
        group = get_object_or_404(Group, name='Docente')
        url = super().form_valid(form)
        self.object.groups.add(group)
        
        return url
