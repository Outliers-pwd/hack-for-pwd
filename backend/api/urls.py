from django.urls import path
from .views import *  # Ensure you import your views correctly
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register-user'),
    path('login/', UserLoginAPIView.as_view(), name='login-user'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout-user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('user/', UserInfoAPIView.as_view(), name='user-info'),

    path('users/', views.users_list, name='users'),
    path('users/<str:pk>/', views.user_detail, name='user-detail'),
    
    path('disabilities/', views.create_disability_list, name='disability-list'),
    path('disabilities/<str:pk>/', views.disability_detail, name='disability-detail'),
    
    path('fitness/', views.fitness_list_create, name='fitness-list-create'),
    path('fitness/<str:pk>/', views.fitness_detail, name='fitness-detail'),
    
    path('devices/', views.device_list_create, name='devices-list'),
    path('device/<str:pk>/', views.device_detail, name='device-detail'),
    
    path('reminders/', views.reminder_list_create, name='reminder_list_create'),
    path('reminders/<int:pk>/', views.reminder_detail, name='reminder_detail'),
    
    path('onboarding-preferences/', views.onboarding_preferences_list_create, name='onboarding_preferences_list_create'),
    path('onboarding-preferences/<int:pk>/', views.onboarding_preferences_detail, name='onboarding_preferences_detail'),
]
