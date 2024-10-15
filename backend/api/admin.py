from django.contrib import admin
from .models import UserModel, FitnessPlan, MentalHealthSession, NutritionPlan, CommunityPost, ProgressTracking, TeleHealthAppointment, Reward

admin.site.register(UserModel)
admin.site.register(FitnessPlan)
admin.site.register(MentalHealthSession)
admin.site.register(NutritionPlan)
admin.site.register(CommunityPost)
admin.site.register(ProgressTracking)
admin.site.register(TeleHealthAppointment)
admin.site.register(Reward)


