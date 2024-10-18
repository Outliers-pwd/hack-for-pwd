from rest_framework.serializers import ModelSerializer
from .models import User, Disability, Fitness, Device, Reminder, OnBoardingPreferences

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'first_name', 'email', 'gender', 'bio', 'username']

class DisabilitySerializer(ModelSerializer):
    class Meta:
        model = Disability
        fields = ['id', 'user', 'disability_type']

class FitnessSerializer(ModelSerializer):
    class Meta:
        model = Fitness
        fields = ['id', 'user', 'fitness_goal', 'workout_type', 'duration', 'intensity_level', 'date', 'progress']

class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'user', 'device_type', 'description']

class ReminderSerializer(ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'user', 'reminder_type', 'reminder_time', 'frequency', 'notes']

class OnBoardingSerializer(ModelSerializer):
    class Meta:
        model = OnBoardingPreferences
        fields = ['id', 'user', 'preferences_field1', 'preferences_field2']
