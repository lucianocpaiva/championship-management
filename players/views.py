# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import PlayerSerializer
from .models import Player

class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('-id')
    serializer_class = PlayerSerializer
    # permission_classes = [permissions.IsAuthenticated]
