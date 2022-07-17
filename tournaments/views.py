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

    @action(detail=True, methods=['post'], url_path='teams', name='teste', serializer_class=TournamentTeamSerializer)
    def teams(self, request, pk=None):

        tournament = get_object_or_404(Tournament, pk=pk)
        
        serializer = TournamentTeamSerializer(data=request.data)
        
        if serializer.is_valid():
            team = Team.objects.get(id=serializer.validated_data['team_id'])
            tournament.teams.add(team)
            tournament.save()
            return Response(serializer.data)
        
        raise exceptions.ValidationError(serializer.errors)

    @teams.mapping.get
    def list_teams(self, request, pk=None):
        tournament = get_object_or_404(Tournament, pk=pk)
        teams = tournament.teams.all()
        serializer = TeamSerializer(teams, many=True, context={'request': request})
        
        return Response(serializer.data)
        

    @action(detail=True, methods=['delete'], url_path='teams/(?P<team_id>[^/.]+)', name='delete-team', serializer_class=TournamentTeamSerializer)
    def delete_teams(self, request, pk=None, team_id=None):
        tournament = get_object_or_404(Tournament, pk=pk)
    
        team = tournament.teams.filter(id=team_id)
        
        if team:
            tournament.teams.remove(team_id)
            tournament.save()
            return Response(status=204)

        raise exceptions.ValidationError('Team not in tournament')







# class TournamentTeamViewSet(viewsets.ModelViewSet):
#     serializer_class = TournamentTeamSerializer
#     http_method_names = ['get', 'post', 'head', 'delete']

#     def get_queryset(self):
#         tournament_pk = self.kwargs['tournament_pk']

#         tournament = Tournament.objects.filter(id=tournament_pk)

#         if not tournament:
#             raise exceptions.NotFound('Tournament not found')
            
#         return tournament.first().teams.all() 

# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser

# class TournamentTeamViewSet(viewsets.ViewSet):
#     serializer_class = TournamentTeamSerializer

#     def list(self, request, tournament_pk=None):
#         # tournament = Tournament.objects.filter(pk=tournament_pk)

#         tournament_teams = self.get_queryset()
#         serializer = TournamentTeamSerializer(tournament_teams, many=True)

#         return Response(serializer.data)

#     def create(self, request, tournament_pk=None):

#         data = JSONParser().parse(request)
#         serializer = TournamentTeamSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

#     def get_queryset(self):
        
#         tournament_pk = self.kwargs['tournament_pk']

#         tournament = Tournament.objects.filter(pk=tournament_pk)

#         if not tournament:
#             raise exceptions.NotFound('Tournament not found')
            
#         return tournament.get().teams.all()

