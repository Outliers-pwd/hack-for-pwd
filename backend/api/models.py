from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENDER_OPTIONS = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('prefer_not_to_say', 'Prefer not to say')
    ]

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True, null=False)
    gender = models.CharField(max_length=50, blank=True, null=True, choices=GENDER_OPTIONS)
    bio = models.TextField(null=True, blank=True)
    username = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Disability(models.Model):
    DISABILITY_CHOICES = [
        ('blind', 'Blind'),
        ('physical', 'Physical Disability'),
        ('deaf', 'Deaf'),
        ('intellectual-disability', 'Intellectual Disability'),
        ('mental-disorders', 'Mental Disorders'),
        ('neurological-disabilities', 'Neurological Disabilities'),
        ('other', 'Other')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disabilities')
    disability_type = models.CharField(max_length=50, choices=DISABILITY_CHOICES)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.get_disability_type_display()}"

class Fitness(models.Model):
    WORKOUT_OPTIONS = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength Training'),
        ('flexibility', 'Flexibility'),
        ('balance', 'Balance'),
        ('high_intensity', 'High-Intensity Interval Training (HIIT)'),
        ('endurance', 'Endurance Training'),
        ('circuit', 'Circuit Training'),
        ('yoga', 'Yoga'),
        ('pilates', 'Pilates'),
        ('aerobics', 'Aerobics'),
        ('sports', 'Sports'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fitness_records')
    fitness_goal = models.TextField(null=True, blank=True)  # Fitness goals eg weight gain, loss etc
    workout_type = models.CharField(max_length=100, null=True, blank=True, choices=WORKOUT_OPTIONS)
    duration = models.IntegerField(null=True, blank=True)
    intensity_level = models.CharField(max_length=50, null=True, blank=True)  # low, medium, high
    date = models.DateField(auto_now_add=True)  # Date when the workout is logged
    progress = models.FloatField(default=0.0)  # Progress towards the goal (percentage)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.fitness_goal}"
    

class Device(models.Model):
    DEVICES_CHOICES = [
        ('wheelchair', 'Wheelchair'),
        ('hearing_aid', 'Hearing Aid'),
        ('assertive_tech', 'Assertive Technology'),
        ('prosthetic', 'Prosthetic'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    device_type = models.CharField(max_length=50, choices=DEVICES_CHOICES)
    description = models.TextField(null=True, blank=True)  # Optional description of the device

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.get_device_type_display()}"


class Reminder(models.Model):
    REMINDER_OPTIONS = [
        ('water_intake', 'Water Intake'),
        ('workout', 'Workout'),
        ('meditation', 'Meditation'),
        ('meal', 'Meal'),
        ('other', 'Other'),
    ]

    FREQUENCY_OPTIONS = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reminders')
    reminder_type = models.CharField(max_length=50, choices=REMINDER_OPTIONS)
    reminder_time = models.TimeField(null=True, blank=True)
    frequency = models.CharField(max_length=50, choices=FREQUENCY_OPTIONS, null=True, blank=True)  # eg daily, weekly
    notes = models.TextField(null=True, blank=True)  # Additional notes or instructions

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.get_reminder_type_display()}"

class OnBoardingPreferences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='onboarding_preferences')
    preference_1 = models.CharField(max_length=255, null=True, blank=True)
    preference_2 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Preferences"
