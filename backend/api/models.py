from django.db import models
from django.contrib.auth.models import User

class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    disability = models.CharField(max_length=255)
    fitness_level = models.CharField(max_length=50)
    goals = models.TextField()
    preferences = models.JSONField(blank=True, null=True)

class FitnessPlan(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField()
    audio_instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MentalHealthSession(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    session_type = models.CharField(max_length=100) # e.g guided meditation, telehealth
    details = models.TextField()
    scheduled_at = models.DateTimeField() #for appointments
    created_at = models.DateTimeField(auto_now_add=True)

class NutritionPlan(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=50)
    description = models.TextField()
    dietary_restrictions = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CommunityPost(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(UserModel, related_name='liked_posts', blank=True)

class ProgressTracking(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    metric = models.CharField(max_length=100) #eg weight, calories burned
    value = models.FloatField()
    recorded = models.DateTimeField(auto_now_add=True)

class TeleHealthAppointment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    professional_name = models.CharField(max_length=255)
    appointment_time = models.DateTimeField()
    session_link= models.URLField()
    notes = models.TextField(blank=True, null=True)

class Reward(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    badge_name = models.CharField(max_length=255)
    awarded_at = models.DateTimeField(auto_now_add=True)