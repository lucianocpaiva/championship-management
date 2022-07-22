from rest_framework import serializers

from .models import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):

    players = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='player-detail'
    )

    class Meta:
        model = Team
        fields = ('id', 'name', 'city', 'state', 'country',
                  'founded', 'stadium', 'url', 'players')
