from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from fish.models import Fish
from fish.serializer import FishSerializer

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from fish.models import Fish
from fish.serializer import FishSerializer


# Create your views here.


class FishViewSet(viewsets.ModelViewSet):

    queryset = Fish.objects.all()
    serializer_class = FishSerializer



#class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    #def __init__(self, data, **kwargs):
        #content = JSONRenderer().render(data)
        #kwargs['content_type'] = 'application/json'
        #super(JSONResponse, self).__init__(content, **kwargs)



#@csrf_exempt
#def fish_list(request):
    """
    List all fishes, or creates a new fish.
    """
    #if request.method == 'GET':
        #fish = Fish.objects.all()
        #serializer = FishSerializer(fish, many=True)
        #return JSONResponse(serializer.data)

    #elif request.method == 'POST':
        #data = JSONParser().parse(request)
        #serializer = FishSerializer(data=data)
        #if serializer.is_valid():
            #serializer.save()
            #return JSONResponse(serializer.data, status=201)
        #return JSONResponse(serializer.errors, status=400)




#@csrf_exempt
#def fish_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    #try:
        #fish = Fish.objects.get(pk=pk)
    #except Fish.DoesNotExist:
        #return HttpResponse(status=404)

    #if request.method == 'GET':
        #serializer = FishSerializer(fish)
        #return JSONResponse(serializer.data)

    #elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        #serializer = FishSerializer(Fish, data=data)
        #if serializer.is_valid():
            #serializer.save()
            #return JSONResponse(serializer.data)
        #return JSONResponse(serializer.errors, status=400)

    #elif request.method == 'DELETE':
        #fish.delete()
        #return HttpResponse(status=204)
