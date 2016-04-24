

from fish.models import Fish
from rest_framework import serializers

class FishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fish
        fields = ('code','weight','type','species','latitude','longitude','photo','classified')

