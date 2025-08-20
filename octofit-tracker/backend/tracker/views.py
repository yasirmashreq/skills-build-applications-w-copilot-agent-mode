

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import UserProfile, Activity, Team, Leaderboard, Workout
from .serializers import UserProfileSerializer, ActivitySerializer, TeamSerializer, LeaderboardSerializer, WorkoutSerializer

import os
from urllib.parse import urljoin

@api_view(['GET'])
def api_root(request, format=None):
	codespace_name = os.environ.get('CODESPACE_NAME')
	if codespace_name:
		base_url = f"https://{codespace_name}-8000.app.github.dev/"
	else:
		base_url = request.build_absolute_uri('/')
	return Response({
		'users': urljoin(base_url, 'api/users/'),
		'activities': urljoin(base_url, 'api/activities/'),
		'teams': urljoin(base_url, 'api/teams/'),
		'leaderboard': urljoin(base_url, 'api/leaderboard/'),
		'workouts': urljoin(base_url, 'api/workouts/'),
	})

class UserProfileListCreate(generics.ListCreateAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

class ActivityListCreate(generics.ListCreateAPIView):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

class TeamListCreate(generics.ListCreateAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class LeaderboardListCreate(generics.ListCreateAPIView):
	queryset = Leaderboard.objects.all()
	serializer_class = LeaderboardSerializer

class WorkoutListCreate(generics.ListCreateAPIView):
	queryset = Workout.objects.all()
	serializer_class = WorkoutSerializer
