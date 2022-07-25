from rest_framework import viewsets, permissions, status, exceptions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from drf_yasg import openapi

from django.utils.decorators import method_decorator

from .serializers import MatchSerializer
from .models import Match
from tournaments.models import Tournament

from .serializers import EventSerializer
from .models import Event

from .services import send_match_event

event_params = [
    openapi.Parameter("tournament_id", openapi.IN_PATH, description="An integer identifying the tournament", type=openapi.TYPE_INTEGER),
    openapi.Parameter("match_id", openapi.IN_PATH, description="An integer identifying the match", type=openapi.TYPE_INTEGER)
]

match_params = [
    openapi.Parameter("tournament_id", openapi.IN_PATH, description="An integer identifying the tournament", type=openapi.TYPE_INTEGER),
]

@method_decorator(name="list", decorator=swagger_auto_schema(tags=['matches'], manual_parameters=match_params))
@method_decorator(name="create", decorator=swagger_auto_schema(tags=['matches'], manual_parameters=match_params))
@method_decorator(name="retrieve", decorator=swagger_auto_schema(tags=['matches'], manual_parameters=match_params))
@method_decorator(name="update", decorator=swagger_auto_schema(tags=['matches'], manual_parameters=match_params))
@method_decorator(name="partial_update", decorator=swagger_auto_schema(tags=['matches'], manual_parameters=match_params))
@method_decorator(name="destroy", decorator=swagger_auto_schema(tags=['matches'], manual_parameters=match_params))
class MatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows matches to be viewed or edited.
    """
    serializer_class = MatchSerializer
    lookup_field = 'id'
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        tournament_id = self.kwargs.get('tournament_id', None)

        if(tournament_id):
            try:
                tournament = Tournament.objects.get(id=tournament_id)

                return Match.objects.filter(tournament=tournament)

            except Tournament.DoesNotExist:
                raise exceptions.NotFound('Tournament not found')

        raise exceptions.NotFound('Tournament not found')


class EventViewSet(viewsets.ViewSet):
    """
    API endpoint that allows events to be viewed.
    """

    @swagger_auto_schema(tags=['events'], manual_parameters=event_params)
    def list(self, request, match_id, tournament_id):
        if not self.get_match(match_id, tournament_id):
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Match not found'})

        events = Event.objects.filter(match_id=match_id)

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['events'], request_body=EventSerializer, manual_parameters=event_params)
    def create(self, request, tournament_id=None, match_id=None):
        match = self.get_match(match_id, tournament_id)

        if not match:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Match not found'})

        serializer = EventSerializer(
            data=request.data, context={'match': match})

        if serializer.is_valid():
            serializer.save()

            payload = {
                **serializer.data,
                match_id: match.id,
            }
            # Send events to message queue
            send_match_event(payload)

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get_match(self, match_id=None, tournament_id=None):
        try:
            return Match.objects.get(id=match_id, tournament_id=tournament_id)
        except Match.DoesNotExist:
            return None
