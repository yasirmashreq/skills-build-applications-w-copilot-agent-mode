from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('users/', views.UserProfileListCreate.as_view(), name='user-list-create'),
    path('activities/', views.ActivityListCreate.as_view(), name='activity-list-create'),
    path('teams/', views.TeamListCreate.as_view(), name='team-list-create'),
    path('leaderboard/', views.LeaderboardListCreate.as_view(), name='leaderboard-list-create'),
    path('workouts/', views.WorkoutListCreate.as_view(), name='workout-list-create'),
]
