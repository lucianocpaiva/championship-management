from unicodedata import name
from django.shortcuts import get_object_or_404

from rest_framework import exceptions
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import action
from teams.serializers import TeamSerializer


from tournaments.serializers import TournamentSerializer, TournamentTeamSerializer
from tournaments.models import Tournament
from teams.models import Team


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    lookup_field = 'id'

    @action(detail=True, methods=['post'], url_path='teams', name='teste', serializer_class=TournamentTeamSerializer)
    def teams(self, request, id=None):

        tournament = get_object_or_404(Tournament, pk=id)
        
        serializer = TournamentTeamSerializer(data=request.data)
        
        if serializer.is_valid():
            team = Team.objects.get(id=serializer.validated_data['team_id'])
            tournament.teams.add(team)
            tournament.save()
            return Response(serializer.data)
        
        raise exceptions.ValidationError(serializer.errors)

    @teams.mapping.get
    def list_teams(self, request, id=None):
        tournament = get_object_or_404(Tournament, pk=id)
        teams = tournament.teams.all()
        serializer = TeamSerializer(teams, many=True, context={'request': request})
        
        return Response(serializer.data)
        

    @action(detail=True, methods=['delete'], url_path='teams/(?P<team_id>[^/.]+)', name='delete-team', serializer_class=TournamentTeamSerializer)
    def delete_teams(self, request, id=None, team_id=None):
        tournament = get_object_or_404(Tournament, pk=id)
    
        team = tournament.teams.filter(id=team_id)
        
        if team:
            tournament.teams.remove(team_id)
            tournament.save()
            return Response(status=204)

        raise exceptions.ValidationError('Team not in tournament')


