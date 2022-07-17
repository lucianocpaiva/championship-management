from rest_framework import serializers

from .models import Transfer
from teams.models import Team
from players.models import Player

class TransferSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        
        team = Team.objects.get(id=validated_data['team'].id)

        # import pdb;pdb.set_trace()

        player = Player.objects.get(id=validated_data['player'].id)

        if player.team == team:
            raise serializers.ValidationError('Passed player is already in this team')

        player.team = team
        player.save()

        transfer = Transfer.objects.create(**validated_data)

        return transfer

    class Meta:
        model = Transfer
        fields = ('id', 'player', 'team', 'date', 'price', 'url')
        
    