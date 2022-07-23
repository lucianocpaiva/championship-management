from rest_framework import serializers, exceptions
from tournaments.models import Tournament
from django.shortcuts import get_object_or_404

from .models import Event
from .models import Match


class MatchSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        tournament = self.validate_data(validated_data)
        
        validated_data['tournament'] = tournament

        return Match.objects.create(**validated_data)

    def update(self, instance, validated_data):
        tournament = self.validate_data(validated_data)
        
        instance.team_home = validated_data.get('team_home', instance.team_home)
        instance.team_away = validated_data.get('team_away', instance.team_away)
        instance.date = validated_data.get('date', instance.date)
        instance.tournament = tournament
        instance.save()
        
        return instance
    
    def validate_data(self, validated_data):
        try:
            tournament = Tournament.objects.get(id=self.context['view'].kwargs['tournament_id'])
        except Tournament.DoesNotExist:
            raise exceptions.NotFound({'message': 'Tournament not found'}) 
            
        if validated_data['team_home'] == validated_data['team_away']:
            err = exceptions.ValidationError({'message': 'Teams cannot be the same'})
            err.status_code = 409
            raise err
        
        return tournament

    class Meta:
        model = Match
        fields = ('id', 'team_home', 'team_away', 'date')


class EventSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        validated_data['match'] = self.context.get('match', None)

        return Event.objects.create(**validated_data)

    class Meta:
        model = Event
        fields = ('id', 'type', 'title', 'description',)
