from rest_framework import serializers
from tournaments.models import Tournament
from django.shortcuts import get_object_or_404

from .models import Event
from .models import Match


class MatchSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):

        if validated_data['team_home'] == validated_data['team_away']:
            raise serializers.ValidationError({'team_home': 'Teams cannot be the same'})
        
        try:
            tournament = get_object_or_404(Tournament, id=self.context['view'].kwargs['tournament_id'], )
        except Tournament.DoesNotExist:
            raise serializers.ValidationError({'tournament': 'Tournament not found'})
        
        validated_data['tournament'] = tournament
        
        return Match.objects.create(**validated_data)
    
    class Meta:
        model = Match
        fields = ('id', 'team_home', 'team_away', 'tournament', 'date')


class EventSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        
        validated_data['match'] = self.context.get('match', None)
        
        return Event.objects.create(**validated_data)
    
    class Meta:
        model = Event
        fields = ('id', 'type', 'title', 'description')
