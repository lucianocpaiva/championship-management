from rest_framework import serializers, status

from .models import Tournament, TournamentTeam
from teams.models import Team

from championship_management.exceptions import HTTPException

class TournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'date', 'teams')
        read_only_fields = ('teams',)

class TournamentTeamSerializer(serializers.ModelSerializer):
        
    def to_internal_value(self, data):
        
        tournament_id = self.context['view'].kwargs['tournament_id']
        
        if not tournament_id.isdigit():
            raise serializers.ValidationError({'message': 'tournament_id must be an integer'})
        
        try:
            tournament = Tournament.objects.get(id=tournament_id)
        except Tournament.DoesNotExist:
            raise HTTPException({'message': 'Tournament not found'}, status.HTTP_404_NOT_FOUND)

        internal = super().to_internal_value(data)
        internal['tournament'] = tournament
    
        return internal
        
    def validate(self, data):
        team = data.get('team', None)
        tournament = data.get('tournament', None)
        
        if team in tournament.teams.all():
            raise HTTPException({'message': 'Team already registered'}, status.HTTP_409_CONFLICT)
  
        return data
    
    class Meta:
        model = TournamentTeam
        fields = ('id', 'team', 'date')
        read_only_fields = ('tournament',)