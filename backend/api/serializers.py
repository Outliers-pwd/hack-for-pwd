from rest_framework import serializers
from .models import User, Disability, Fitness, Device, Reminder, OnBoardingPreferences
from django.contrib.auth import authenticate


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password1", "password2")

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match!")

        password = attrs.get("password1", "")
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters!")

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password1")
        validated_data.pop("password2")
        return User.objects.create_user(password=password, **validated_data)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials!")


class DisabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Disability
        fields = ['id', 'user', 'disability_type']


class FitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fitness
        fields = ['id', 'user', 'fitness_goal', 'workout_type', 'duration', 'intensity_level', 'date', 'progress']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'user', 'device_type', 'description']


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'user', 'reminder_type', 'reminder_time', 'frequency', 'notes']


class OnBoardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnBoardingPreferences
        fields = ['id', 'user', 'preferences_field1', 'preferences_field2']
