from django.contrib import admin
from .models import User, Disability, Fitness, Reminder, Device

admin.site.register(User)
admin.site.register(Disability)
admin.site.register(Fitness)
admin.site.register(Device)
admin.site.register(Reminder)