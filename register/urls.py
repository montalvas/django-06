from django.urls import path
from .views import FieldCreate, ActivityCreate

app_name = 'register'

urlpatterns = [
    path('field/', FieldCreate.as_view(), name='register-field'),
    path('activity/', ActivityCreate.as_view(), name='register-activity'),
]
