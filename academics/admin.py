'''
This file is responsible for registering the models in the academic app in the admin panel.
A specialized ModelAdmin has been created for Class_LevelAdmin.
'''
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Subject, Class_Level

# This is a specialized ModelAdmin for Class_LevelAdmin where some parameters have been modified
# to enhance the display and usage of the Class_Level model in the admin panel.
class Class_LevelAdmin(ModelAdmin):
    model = Class_Level # This links the modeladmin to the model.
    list_display = ['class_name', 'class_stream', 'class_teacher'] # Specifies the fields to display in the Class_Level admin homepage.
    ordering = ['class_name', 'academic_year'] # Specifies the fields which should be used for the ordering of the Class_Level instances.
    list_filter = ['class_name', 'academic_year'] # Specifies the fields which should be used to filter the instances of the Class_Level instances.

    # These are the fields which will be filled manually to create an instance of the Class_Level model.
    fieldsets = (
        (None, {'fields': ('class_name', 'class_stream', 'class_teacher',
                           'subject_teachers', 'academic_year')}),
    )

admin.site.register(Subject) # Register the Subject model in the admin panel.
admin.site.register(Class_Level, Class_LevelAdmin) # Register the Class_Level model in the admin panel.