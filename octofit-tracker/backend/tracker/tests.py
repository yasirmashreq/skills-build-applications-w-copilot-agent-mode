
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import UserProfile, Activity, Team

class UserProfileTests(APITestCase):
	def setUp(self):
		self.user = UserProfile.objects.create(username='testuser', email='test@example.com', display_name='Test User')

	def test_user_profile_created(self):
		self.assertEqual(UserProfile.objects.count(), 1)
		self.assertEqual(self.user.username, 'testuser')

	def test_user_profile_api(self):
		url = reverse('user-list-create')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class ActivityTests(APITestCase):
	def setUp(self):
		self.user = UserProfile.objects.create(username='activityuser', email='activity@example.com', display_name='Activity User')
		self.activity = Activity.objects.create(user=self.user, activity_type='Running', duration_minutes=30, calories_burned=300, date='2025-08-20')

	def test_activity_created(self):
		self.assertEqual(Activity.objects.count(), 1)
		self.assertEqual(self.activity.activity_type, 'Running')

	def test_activity_api(self):
		url = reverse('activity-list-create')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

class TeamTests(APITestCase):
	def setUp(self):
		self.user = UserProfile.objects.create(username='teamuser', email='team@example.com', display_name='Team User')
		self.team = Team.objects.create(name='Team A')
		self.team.members.add(self.user)

	def test_team_created(self):
		self.assertEqual(Team.objects.count(), 1)
		self.assertEqual(self.team.name, 'Team A')

	def test_team_api(self):
		url = reverse('team-list-create')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
