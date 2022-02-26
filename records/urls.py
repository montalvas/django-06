from django.urls import path
from .views import FieldCreate, ActivityCreate
from .views import FieldUpdate, ActivityUpdate
from .views import FieldDelete, ActivityDelete
from .views import FieldList, ActivityList

app_name = 'records'

urlpatterns = [
    # register
    path('register/field/', FieldCreate.as_view(), name='register-field'),
    path('register/activity/', ActivityCreate.as_view(), name='register-activity'),
    
    # update
    path('update/field/<int:pk>', FieldUpdate.as_view(), name='update-field'),
    path('update/activity/<int:pk>', ActivityUpdate.as_view(), name='update-activity'),
    
    # delete
    path('delete/field/<int:pk>', FieldDelete.as_view(), name='delete-field'),
    path('delete/activity/<int:pk>', ActivityDelete.as_view(), name='delete-activity'),
    
    # lista
    path('list/field', FieldList.as_view(), name='list-field'),
    path('list/activity', ActivityList.as_view(), name='list-activity'),
    
]
