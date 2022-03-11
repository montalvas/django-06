from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserCreate, ProfileUpdate


app_name = 'auth'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'
    ), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('register/', UserCreate.as_view(), name='register'),
    
    path('update-profile/', ProfileUpdate.as_view(), name='update-profile'),
]
