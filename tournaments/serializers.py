from rest_framework import serializers

from .models import Tournament
from teams.models import Team

class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    
    teams = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='team-detail'
    )

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'date', 'teams')

class TournamentTeamSerializer(serializers.Serializer):
    team_id = serializers.IntegerField()
    
