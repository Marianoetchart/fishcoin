from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from fish.models import Fish
from fish.serializer import FishSerializer


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from fish.models import Fish, ClassifyFish
from fish.serializer import FishSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fish.models import Fish
from fish.serializer import FishSerializer
from binascii import a2b_base64
import requests


# Create your views here.



import time; start_time = time.time()
import warnings; warnings.filterwarnings('ignore');
import numpy as np
import pandas as pd
from PIL import Image
from PIL import ImageFilter
import os
import glob
from scipy import misc
from sklearn import svm
import pickle
import io
import urllib
from binascii import a2b_base64



class FishViewSet(viewsets.ModelViewSet):

    queryset = Fish.objects.all()
    serializer_class = FishSerializer


def ClassifyFish(url):


    data = url
    binary_data = a2b_base64(data)

    fd = open('image.png', 'wb')
    fd.write(binary_data)
    fd.close()


    #file = io.BytesIO(urllib.urlopen(url).read())
    im = Image.open('image.png')
    im = im.resize((500, 500), Image.ANTIALIAS) #Could increase resolution which might improve accuracy
    image = np.reshape(np.array(im.getdata()).flatten(),(np.array(im.getdata()).flatten().shape[0],1))

    with open('Scaled_model.pkl', 'rb') as fid:
        gnb_loaded = pickle.load(fid)

    return gnb_loaded.predict(np.transpose(image))










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

        ClassifyFish(request.data['photo'])
        serializer = FishSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









