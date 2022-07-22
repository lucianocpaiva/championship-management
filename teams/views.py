from rest_framework import viewsets
from rest_framework import permissions

from teams.serializers import TeamSerializer
from teams.models import Team


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
