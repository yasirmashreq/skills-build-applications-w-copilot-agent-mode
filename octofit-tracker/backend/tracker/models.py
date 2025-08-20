
from django.db import models

class UserProfile(models.Model):
	username = models.CharField(max_length=150, unique=True)
	email = models.EmailField(unique=True)
	display_name = models.CharField(max_length=150)
	bio = models.TextField(blank=True)
	def __str__(self):
		return self.username

class Activity(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	activity_type = models.CharField(max_length=100)
	duration_minutes = models.PositiveIntegerField()
	calories_burned = models.PositiveIntegerField()
	date = models.DateField()
	def __str__(self):
		return f"{self.user.username} - {self.activity_type} on {self.date}"

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	members = models.ManyToManyField(UserProfile, related_name='teams')
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name
