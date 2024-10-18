from django.urls import path
from .import views

urlpatterns = [
    # USER URLS
    path('users/', views.users_list, name='users'),
    path('users/<str:pk>/', views.user_detail, name='user-detail'),

    # DISABILITY URLS
    path('disabilities/', views.create_disability_list, name='disability-list'),
    path('disabilities/<str:pk>/', views.disability_detail, name='disability-detail'),

    # FITNESS URLS
    path('fitness/', views.fitness_list_create, name='fitness-list-create'),
    path('fitness/<str:pk>/', views.fitness_detail, name='fitness-detail'),

    #DEVICE URLS
    path('devices/', views.device_list_create, name='devices-list'),
    path('device/<str:pk>/', views.device_detail, name='device-detail'),

    # REMINDER URLS
    path('reminders/', views.reminder_list_create, name='reminder_list_create'),
    path('reminders/<int:pk>/', views.reminder_detail, name='reminder_detail'),

    # ONBOARDING PREFERENCES
    path('onboarding-preferences/', views.onboarding_preferences_list_create, name='onboarding_preferences_list_create'),
    path('onboarding-preferences/<int:pk>/', views.onboarding_preferences_detail, name='onboarding_preferences_detail'),
]