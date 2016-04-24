from django.db import models

# Create your models here.


class Fish(models.Model):
        code = models.CharField(max_length=255)
        #created = models.DateTimeField('auto_now_add=True')
        weight = models.CharField(max_length=255)
        type = models.CharField(max_length=255)
        species = models.CharField(max_length=255)
        latitude  = models.FloatField()
        longitude = models.FloatField()
        photo = models.TextField(max_length='')
        classified = models.CharField(max_length=255)

        def __str__(self):
                return  self.code

        #class Meta:
                #ordering = ['code']




#{class CachedImage(models.Model):
    #url = models.CharField(max_length=255, unique=True)
    #photo = models.ImageField(upload_to=photo_path, blank=True)

    #def cache(self):
        """Store image locally if we have a URL"""

        #if self.url and not self.photo:
            #result = urllib.urlretrieve(self.url)
            #self.photo.save(
                    #os.path.basename(self.url),
                    #File(open(result[0]))
                    # )
            #self.save()

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





def ClassifyFish(url):
    file = io.BytesIO(urllib.urlopen(url).read())
    im = Image.open(file)
    im = im.resize((500, 500), Image.ANTIALIAS) #Could increase resolution which might improve accuracy
    image = np.reshape(np.array(im.getdata()).flatten(),(np.array(im.getdata()).flatten().shape[0],1))

    with open('Scaled_model.pkl', 'rb') as fid:
        gnb_loaded = pickle.load(fid)

    return gnb_loaded.predict(np.transpose(image))


