from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import UserForm


class UserCreate(CreateView):
    template_name = 'users/register.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('website:index')
