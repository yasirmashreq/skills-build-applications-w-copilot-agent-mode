

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import UserProfile, Activity, Team, Leaderboard, Workout
from .serializers import UserProfileSerializer, ActivitySerializer, TeamSerializer, LeaderboardSerializer, WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list-create', request=request, format=format),
		'activities': reverse('activity-list-create', request=request, format=format),
		'teams': reverse('team-list-create', request=request, format=format),
		'leaderboard': reverse('leaderboard-list-create', request=request, format=format),
		'workouts': reverse('workout-list-create', request=request, format=format),
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
