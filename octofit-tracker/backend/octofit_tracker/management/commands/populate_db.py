from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='john.doe@example.com', name='John Doe', age=25, team='Blue Team'),
            User(email='jane.smith@example.com', name='Jane Smith', age=30, team='Red Team'),
            User(email='alice.jones@example.com', name='Alice Jones', age=22, team='Blue Team'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(name='Blue Team', members=[{'email': 'john.doe@example.com'}, {'email': 'alice.jones@example.com'}]),
            Team(name='Red Team', members=[{'email': 'jane.smith@example.com'}]),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Running', duration=30, date=date(2025, 4, 1)),
            Activity(user=users[1], activity_type='Cycling', duration=45, date=date(2025, 4, 2)),
            Activity(user=users[2], activity_type='Swimming', duration=60, date=date(2025, 4, 3)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=teams[0], points=100),
            Leaderboard(team=teams[1], points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Morning Run', description='A quick morning run to start the day', duration=30),
            Workout(name='Evening Yoga', description='Relaxing yoga session', duration=60),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
