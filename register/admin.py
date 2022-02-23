from django.contrib import admin
from .models import Field, Activity


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'updated', 'activated']
    
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['number', 'description', 'points', 'details', 'field', 'updated', 'activated']
