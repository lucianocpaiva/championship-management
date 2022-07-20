import resource
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema

from .serializers import MatchSerializer
from .models import Match

from django.utils.decorators import method_decorator
from rest_framework.decorators import action

@method_decorator(name="list", decorator=swagger_auto_schema(tags=['matches']))
@method_decorator(name="create", decorator=swagger_auto_schema(tags=['matches']))
@method_decorator(name="retrieve", decorator=swagger_auto_schema(tags=['matches']))
@method_decorator(name="update", decorator=swagger_auto_schema(tags=['matches']))
@method_decorator(name="partial_update", decorator=swagger_auto_schema(tags=['matches']))
@method_decorator(name="destroy", decorator=swagger_auto_schema(tags=['matches']))
@method_decorator(name="events", decorator=swagger_auto_schema(tags=['matches']))
class MatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows matches to be viewed or edited.
    """
    serializer_class = MatchSerializer
    
    def get_queryset(self):
        return Match.objects.filter(tournament=self.kwargs['tournament_id'])


    @action(detail=True, methods=['post'], url_path='events')
    def events(self, request):
       pass
