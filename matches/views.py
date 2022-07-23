from rest_framework import viewsets, permissions, status, exceptions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from django.utils.decorators import method_decorator

from .serializers import MatchSerializer
from .models import Match
from tournaments.models import Tournament

from .serializers import EventSerializer
from .models import Event

from .services import send_match_event


@method_decorator(name="list", decorator=swagger_auto_schema(tags=['matches']))
@method_decorator(name="create", decorator=swagger_auto_schema(tags=['matches']))
@method_decorator(name="retrieve", decorator=swagger_auto_schema(tags=['matches']))
@method_decorator(name="update", decorator=swagger_auto_schema(tags=['matches']))
@method_decorator(name="partial_update", decorator=swagger_auto_schema(tags=['matches']))
@method_decorator(name="destroy", decorator=swagger_auto_schema(tags=['matches']))
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

    @swagger_auto_schema(tags=['events'])
    def list(self, request, match_id, tournament_id):
        if not self.get_match(match_id, tournament_id):
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Match not found'})

        events = Event.objects.filter(match_id=match_id)

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['events'], request_body=EventSerializer)
    def create(self, request, tournament_id=None, match_id=None):
        match = self.get_match(match_id, tournament_id)
        print(match)
        if not match:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Match not found'})

        serializer = EventSerializer(
            data=request.data, context={'match': match})

        if serializer.is_valid():
            serializer.save()

            # Send events to message queue
            send_match_event(match.id, serializer.data)

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get_match(self, match_id=None, tournament_id=None):
        try:
            return Match.objects.get(id=match_id, tournament_id=tournament_id)
        except Match.DoesNotExist:
            return None
