from rest_framework import serializers

from .models import Tournament
from teams.models import Team

class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    
    teams = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='team-detail'
    )

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'date', 'teams')


# class TournamentTeamSerializer(serializers.HyperlinkedModelSerializer):


#     teams = serializers.HyperlinkedRelatedField(
#         many=True,
#         read_only=True,
#         view_name='team-detail'
#     )

#     def create(self, validated_data):
#         tournament = Tournament.objects.get(id=self.context['view'].kwargs['tournament_pk'])
#         team = Team.objects.get(id=validated_data['team_id'])

#         tournament.teams.add(team)
#         tournament.save()

#         return tournament

#     class Meta:
#         model = None
#         fields = ('id', 'name', 'teams')
        

class TournamentTeamSerializer(serializers.Serializer):
    team_id = serializers.IntegerField()
    

        


    # def create(self, validated_data):
    #     import pdb;pdb.set_trace()
    #     # team = Team.objects.get(id=validated_data['team'].id)

    #     team = Team.objects.get(id=validated_data['team_id'])

    #     # Tournament.objects.filter(id=validated_data['tournament'].id).update(teams=team)

    #     tournament = Tournament.objects.get(id=validated_data['tournament'].id)
    #     tournament.teams.add(team)
    #     tournament.save()
        
    #     # import pdb;pdb.set_trace()

    #     # player = Player.objects.get(id=validated_data['player'].id)

    #     # if player.team == team:
    #     #     raise serializers.ValidationError('Passed player is already in this team')

    #     # player.team = team
    #     # player.save()

    #     # transfer = Transfer.objects.create(**validated_data)

    #     return tournament.teams.all()

        
    #     return 'transfer'