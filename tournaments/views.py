from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from drf_yasg import openapi

from rest_framework import exceptions, mixins, viewsets
from drf_yasg.utils import swagger_auto_schema

from tournaments.serializers import TournamentSerializer, TournamentTeamSerializer
from tournaments.models import Tournament, TournamentTeam

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    lookup_field = 'id'


params = [
    openapi.Parameter("tournament_id",
        openapi.IN_PATH,
        description="An integer identifying the tournament",
        type=openapi.TYPE_INTEGER
    )
]

@method_decorator(name="list", decorator=swagger_auto_schema(manual_parameters=params, tags=['tournament-teams']))
@method_decorator(name="create", decorator=swagger_auto_schema(manual_parameters=params, tags=['tournament-teams']))
@method_decorator(name="retrieve", decorator=swagger_auto_schema(manual_parameters=params, tags=['tournament-teams']))
@method_decorator(name="update", decorator=swagger_auto_schema(manual_parameters=params, tags=['tournament-teams']))
@method_decorator(name="partial_update", decorator=swagger_auto_schema(manual_parameters=params, tags=['tournament-teams']))
@method_decorator(name="destroy", decorator=swagger_auto_schema(manual_parameters=params, tags=['tournament-teams']))
class TournamentTeamViewSet(viewsets.ModelViewSet):
    queryset = TournamentTeam.objects.all()
    serializer_class = TournamentTeamSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        tournament_id = self.kwargs.get('tournament_id', None)

        if(tournament_id):
            try:
                tournament = Tournament.objects.get(id=tournament_id)

                return TournamentTeam.objects.filter(tournament=tournament)

            except Tournament.DoesNotExist:
                raise exceptions.NotFound('Tournament not found')
