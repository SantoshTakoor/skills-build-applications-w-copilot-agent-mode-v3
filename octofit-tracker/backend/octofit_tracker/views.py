from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityListCreateView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardListCreateView(generics.ListCreateAPIView):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutListCreateView(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

def api_root(request):
    codespace_url = "https://[SantoshTakoor/skills-build-applications-w-copilot-agent-mode-v3#1]-8000.app.github.dev"
    return Response({
        'users': f'{codespace_url}/api/users/',
        'teams': f'{codespace_url}/api/teams/',
        'activity': f'{codespace_url}/api/activity/',
        'leaderboard': f'{codespace_url}/api/leaderboard/',
        'workouts': f'{codespace_url}/api/workouts/',
    })
