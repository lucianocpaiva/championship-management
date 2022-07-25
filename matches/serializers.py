from rest_framework import serializers, exceptions, status
from tournaments.models import Tournament
from django.shortcuts import get_object_or_404


from championship_management.exceptions import HTTPException
from .models import Event
from .models import Match


class MatchSerializer(serializers.ModelSerializer):

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

        if data['team_home'] == data['team_away']:
            raise HTTPException({'message': 'Teams cannot be the same'}, status.HTTP_409_CONFLICT)
        
        return data

    class Meta:
        model = Match
        fields = ('id', 'team_home', 'team_away', 'date')


class EventSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=(
        'start', 'goal', 'penalty', 'yellow', 'red', 'end', 'substitution', 'break', 'break_start', 'break_end', 'corner'
    ))

    def create(self, validated_data):

        validated_data['match'] = self.context.get('match', None)

        return Event.objects.create(**validated_data)

    class Meta:
        model = Event
        fields = ('id', 'type', 'date', 'description', 'match')
        read_only_fields = ['match']
