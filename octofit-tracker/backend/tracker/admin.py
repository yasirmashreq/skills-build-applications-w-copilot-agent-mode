from django.contrib import admin
from .models import UserProfile, Activity, Team

admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(Team)
