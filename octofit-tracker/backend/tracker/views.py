
from rest_framework import generics
from .models import UserProfile, Activity, Team
from .serializers import UserProfileSerializer, ActivitySerializer, TeamSerializer

class UserProfileListCreate(generics.ListCreateAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

class ActivityListCreate(generics.ListCreateAPIView):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

class TeamListCreate(generics.ListCreateAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
