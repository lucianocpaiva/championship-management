from rest_framework import serializers
from tournaments.models import Tournament
from django.shortcuts import get_object_or_404

from .models import Match


class MatchSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):

        tournament = get_object_or_404(Tournament, id=self.context['view'].kwargs['tournament_id'], )
        
        validated_data['tournament'] = tournament
        return Match.objects.create(**validated_data)
    
    class Meta:
        model = Match
        fields = ('id', 'team', 'team_adversary', 'date') 
