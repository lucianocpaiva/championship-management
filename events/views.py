import resource
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema

from .serializers import EventSerializer
from .models import Event

from django.utils.decorators import method_decorator
from rest_framework.decorators import action


@method_decorator(name="list", decorator=swagger_auto_schema(tags=['events']))
@method_decorator(name="create", decorator=swagger_auto_schema(tags=['events']))
@method_decorator(name="retrieve", decorator=swagger_auto_schema(tags=['events']))
@method_decorator(name="update", decorator=swagger_auto_schema(tags=['events']))
@method_decorator(name="partial_update", decorator=swagger_auto_schema(tags=['events']))
@method_decorator(name="destroy", decorator=swagger_auto_schema(tags=['events']))
class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    serializer_class = EventSerializer
    
    def get_queryset(self):
        return Event.objects.filter()