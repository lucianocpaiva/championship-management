from rest_framework import serializers

from .models import Transfer

class TransferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transfer
        fields = ('id', 'player', 'team', 'date', 'price', 'url')
        