from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Event
from matches.models import Match


class EventSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
     
        match = get_object_or_404(Match, id=self.context['view'].kwargs['match_id'], )
        
        validated_data['match'] = match
        
        return Event.objects.create(**validated_data)
    
    class Meta:
        model = Event
        fields = ('id', 'type', 'title', 'description')
