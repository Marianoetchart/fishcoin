from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from fish.models import Fish
from fish.serializers import FishSerializer

# Create your views here.




class FishViewSet(viewsets.ModelViewSet):

    queryset = Fish.objects.all()
    serializer_class = FishSerializer

