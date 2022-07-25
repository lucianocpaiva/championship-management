from rest_framework import serializers

from .models import Team


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'name', 'city', 'state', 'country', 'coach', 'players')
        read_only_fields = ('players',)
