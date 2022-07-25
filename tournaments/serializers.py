from rest_framework import serializers

from .models import Tournament


class TournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'date', 'teams')
        read_only_fields = ('teams',)

class TournamentTeamSerializer(serializers.Serializer):
    team_id = serializers.IntegerField()
