from rest_framework import serializers

from .models import Transfer
from teams.models import Team
from players.models import Player


class TransferSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        team = Team.objects.get(id=validated_data['team'].id)

        player = Player.objects.get(id=validated_data['player'].id)

        if player.team == team:
            err = serializers.ValidationError(
                'Passed player is already in this team')
            err.status_code = 409
            raise err

        player.team = team
        player.save()

        transfer = Transfer.objects.create(**validated_data)

        return transfer

    def update(self, instance, validated_data):
        instance.team = Team.objects.get(id=validated_data['team'].id)
        instance.player = Player.objects.get(id=validated_data['player'].id)
        instance.date = validated_data['date']
        instance.price = validated_data['price']

        # Update player team
        instance.player.team = instance.team

        instance.player.save()
        instance.save()

        return instance

    class Meta:
        model = Transfer
        fields = ('id', 'player', 'team', 'date', 'price')
