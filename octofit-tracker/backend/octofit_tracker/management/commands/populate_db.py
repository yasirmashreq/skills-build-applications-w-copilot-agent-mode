from django.core.management.base import BaseCommand
from tracker.models import UserProfile, Activity, Team
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            Activity.objects.all().delete()
            Team.objects.all().delete()
            UserProfile.objects.all().delete()

            marvel = Team.objects.create(name='Team Marvel')
            dc = Team.objects.create(name='Team DC')

            # Superhero users
            users = [
                UserProfile(username='ironman', email='ironman@marvel.com', display_name='Iron Man', bio='Genius, billionaire, playboy, philanthropist.'),
                UserProfile(username='captainamerica', email='cap@marvel.com', display_name='Captain America', bio='The first Avenger.'),
                UserProfile(username='spiderman', email='spidey@marvel.com', display_name='Spider-Man', bio='Friendly neighborhood hero.'),
                UserProfile(username='batman', email='batman@dc.com', display_name='Batman', bio='The Dark Knight.'),
                UserProfile(username='superman', email='superman@dc.com', display_name='Superman', bio='Man of Steel.'),
                UserProfile(username='wonderwoman', email='wonderwoman@dc.com', display_name='Wonder Woman', bio='Amazonian warrior princess.'),
            ]
            for user in users:
                user.save()

            marvel.members.add(users[0], users[1], users[2])
            dc.members.add(users[3], users[4], users[5])

            # Activities
            Activity.objects.create(user=users[0], activity_type='Running', duration_minutes=30, calories_burned=300, date='2025-08-19')
            Activity.objects.create(user=users[1], activity_type='Cycling', duration_minutes=45, calories_burned=400, date='2025-08-18')
            Activity.objects.create(user=users[2], activity_type='Swimming', duration_minutes=60, calories_burned=500, date='2025-08-17')
            Activity.objects.create(user=users[3], activity_type='Running', duration_minutes=40, calories_burned=350, date='2025-08-19')
            Activity.objects.create(user=users[4], activity_type='Cycling', duration_minutes=50, calories_burned=420, date='2025-08-18')
            Activity.objects.create(user=users[5], activity_type='Swimming', duration_minutes=70, calories_burned=520, date='2025-08-17')

            self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
