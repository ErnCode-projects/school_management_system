'''
This file handles the registration of models in the admin panel.
'''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Student, Teacher
from .forms import CustomUserModelForm, CustomUserChangeForm


# Because a custom user model was created, a custom useradmin had to be created before registration
# because of the additional fields added to the user model. 
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserModelForm # This connects the custom user admin to the custom user model creation form.
    form = CustomUserChangeForm # This connect the custom user admin to the custom user model editing form.
    model = CustomUser # This connects the custom user admin to the custom user model.
    list_display = ['username', 'last_name', 'first_name', 'other_names', 'role'] # These are the fields that are displayed on the users homepage in the admin panel.
    ordering = ['username', 'last_name', 'first_name', 'other_names'] # These are the fields that can be used to order instances whether in the ascending order or descending order.
    list_filter = ['username', 'last_name', 'first_name', 'other_names', 'role'] # These are the fields that can be used to filter instances.

    # These are the fields availabe in the admin panel when creating a user.
    add_fieldsets = (
        ('Personal Info', {'fields': ('first_name', 'last_name', 'other_names', 'profile_picture', 'gender',
                           'date_of_birth', 'role', 'address', 'emergency_contact')}),
    )

    # These are the fields available in the admin panel when editing a user.
    fieldsets = (
        ('Personal Info', {'fields': ('first_name', 'last_name', 'other_names', 'profile_picture', 'gender',
                           'date_of_birth', 'role', 'address', 'emergency_contact')}),
    )

admin.site.register(CustomUser, CustomUserAdmin) # Register the CustomUser in the admin panel.
admin.site.register(Student) # Register the Student model in the admin panel.
admin.site.register(Teacher) # Register the Teacher model in the admin panel.