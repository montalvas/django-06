from django.urls import path

from .views import FieldCreate, ActivityCreate, StateCreate, CityCreate, CampusCreate, OfficialCreate, StatusCreate, SituationCreate, GradeCreate, ProgressionCreate, ReceiptCreate, ValidationCreate

from .views import FieldUpdate, ActivityUpdate, StateUpdate, CityUpdate, CampusUpdate, OfficialUpdate, StatusUpdate, SituationUpdate, GradeUpdate, ProgressionUpdate, ReceiptUpdate, ValidationUpdate

from .views import FieldDelete, ActivityDelete, StateDelete, CityDelete, CampusDelete, OfficialDelete, StatusDelete, SituationDelete, GradeDelete, ProgressionDelete, ReceiptDelete, ValidationDelete

from .views import FieldList, ActivityList, StateList, CityList, CampusList, OfficialList, StatusList, SituationList, GradeList, ProgressionList, ReceiptList, ValidationList

app_name = 'records'

urlpatterns = [
    # register
    path('register/field/', FieldCreate.as_view(), name='register-field'),
    path('register/activity/', ActivityCreate.as_view(), name='register-activity'),
    path('register/state/', StateCreate.as_view(), name='register-state'),
    path('register/city/', CityCreate.as_view(), name='register-city'),
    path('register/campus/', CampusCreate.as_view(), name='register-campus'),
    path('register/official/', OfficialCreate.as_view(), name='register-official'),
    path('register/status/', StatusCreate.as_view(), name='register-status'),
    path('register/situation/', SituationCreate.as_view(), name='register-situation'),
    path('register/grade/', GradeCreate.as_view(), name='register-grade'),
    path('register/progression/', ProgressionCreate.as_view(), name='register-progression'),
    path('register/receipt/', ReceiptCreate.as_view(), name='register-receipt'),
    path('register/validation/', ValidationCreate.as_view(), name='register-validation'),
    
    # update
    path('update/field/<int:pk>', FieldUpdate.as_view(), name='update-field'),
    path('update/activity/<int:pk>', ActivityUpdate.as_view(), name='update-activity'),
    path('update/state/<int:pk>', StateUpdate.as_view(), name='update-state'),
    path('update/city/<int:pk>', CityUpdate.as_view(), name='update-city'),
    path('update/campus/<int:pk>', CampusUpdate.as_view(), name='update-campus'),
    path('update/official/<int:pk>', OfficialUpdate.as_view(), name='update-official'),
    path('update/status/<int:pk>', StatusUpdate.as_view(), name='update-status'),
    path('update/situation/<int:pk>', SituationUpdate.as_view(), name='update-situation'),
    path('update/grade/<int:pk>', GradeUpdate.as_view(), name='update-grade'),
    path('update/progression/<int:pk>', ProgressionUpdate.as_view(), name='update-progression'),
    path('update/receipt/<int:pk>', ReceiptUpdate.as_view(), name='update-receipt'),
    path('update/validation/<int:pk>', ValidationUpdate.as_view(), name='update-validation'),
    
    # delete
    path('delete/field/<int:pk>', FieldDelete.as_view(), name='delete-field'),
    path('delete/activity/<int:pk>', ActivityDelete.as_view(), name='delete-activity'),
    path('delete/state/<int:pk>', StateDelete.as_view(), name='delete-state'),
    path('delete/city/<int:pk>', CityDelete.as_view(), name='delete-city'),
    path('delete/campus/<int:pk>', CampusDelete.as_view(), name='delete-campus'),
    path('delete/official/<int:pk>', OfficialDelete.as_view(), name='delete-official'),
    path('delete/status/<int:pk>', StatusDelete.as_view(), name='delete-status'),
    path('delete/situation/<int:pk>', SituationDelete.as_view(), name='delete-situation'),
    path('delete/grade/<int:pk>', GradeDelete.as_view(), name='delete-grade'),
    path('delete/progression/<int:pk>', ProgressionDelete.as_view(), name='delete-progression'),
    path('delete/receipt/<int:pk>', ReceiptDelete.as_view(), name='delete-receipt'),
    path('delete/validation/<int:pk>', ValidationDelete.as_view(), name='delete-validation'),
    
    
    # lista
    path('list/field', FieldList.as_view(), name='list-field'),
    path('list/activity', ActivityList.as_view(), name='list-activity'),
    path('list/state', StateList.as_view(), name='list-state'),
    path('list/city', CityList.as_view(), name='list-city'),
    path('list/campus', CampusList.as_view(), name='list-campus'),
    path('list/official', OfficialList.as_view(), name='list-official'),
    path('list/status', StatusList.as_view(), name='list-status'),
    path('list/situation', SituationList.as_view(), name='list-situation'),
    path('list/grade', GradeList.as_view(), name='list-grade'),
    path('list/progression', ProgressionList.as_view(), name='list-progression'),
    path('list/receipt', ReceiptList.as_view(), name='list-receipt'),
    path('list/validation', ValidationList.as_view(), name='list-validation'),
]
