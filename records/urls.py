from django.urls import path
from .views import FieldCreate, ActivityCreate
from .views import FieldUpdate, ActivityUpdate

app_name = 'records'

urlpatterns = [
    # register
    path('register/field/', FieldCreate.as_view(), name='register-field'),
    path('register/activity/', ActivityCreate.as_view(), name='register-activity'),
    
    # update
    path('update/field/<int:pk>', FieldUpdate.as_view(), name='update-field'),
    path('update/activity/<int:pk>', ActivityUpdate.as_view(), name='update-activity'),
    
    # delete
]
