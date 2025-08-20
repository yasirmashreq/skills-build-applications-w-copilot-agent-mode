from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserProfileListCreate.as_view(), name='user-list-create'),
    path('activities/', views.ActivityListCreate.as_view(), name='activity-list-create'),
    path('teams/', views.TeamListCreate.as_view(), name='team-list-create'),
]
