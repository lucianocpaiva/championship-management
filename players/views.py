# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import PlayerSerializer
from .models import Player

from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(tags=['matches'], security=[{'Bearer': []}])
class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('-id')
    serializer_class = PlayerSerializer
    # permission_classes = [permissions.IsAuthenticated]
