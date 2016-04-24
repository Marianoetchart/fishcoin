from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from fish.models import Fish
from fish.serializer import FishSerializer


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from fish.models import Fish
from fish.serializer import FishSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fish.models import Fish
from fish.serializer import FishSerializer

# Create your views here.


class FishViewSet(viewsets.ModelViewSet):

    queryset = Fish.objects.all()
    serializer_class = FishSerializer



@api_view(['GET', 'POST'])
def fish_list(request):
    """
    List all fishes, or create a new fish.
    """
    if request.method == 'GET':
        fish = Fish.objects.all()
        serializer = FishSerializer(fish, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    