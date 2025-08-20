
from django.contrib import admin
from .models import UserProfile, Activity, Team, Leaderboard, Workout

admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(Team)
admin.site.register(Leaderboard)
admin.site.register(Workout)
