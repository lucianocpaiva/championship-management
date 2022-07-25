from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from teams.serializers import TeamSerializer
from teams.models import Team


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'city', 'state', 'country', 'coach']
