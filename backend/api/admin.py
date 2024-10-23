from django.contrib import admin
from .models import User, Disability, Fitness, Device, Reminder, OnBoardingPreferences
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)

class UserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm  # Use the custom creation form
    form = CustomUserChangeForm  # Use the custom change form
    list_display = ("email", "username", "first_name", "last_name", "is_staff")  # Adjust fields displayed in the list
    list_filter = ("is_staff", "is_active")  # Add filters for easier admin navigation
    search_fields = ("email", "username")  # Enable search functionality

# Register the User model with the custom UserAdmin
admin.site.register(User, UserAdmin)
admin.site.register(Disability)
admin.site.register(Fitness)
admin.site.register(Device)
admin.site.register(Reminder)
admin.site.register(OnBoardingPreferences)
