from django.urls import path
from .views import IndexView, AboutView

app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about')
]
