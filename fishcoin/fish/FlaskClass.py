from flask import Flask, jsonify, g, redirect, request, url_for
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
from binascii import a2b_base64

app = Flask(__name__)

@app.route('/classify/')
def ClassifyFish():
    # get number of items from the javascript request
    nitems = request.args.get('photo')

    data = nitems
    binary_data = a2b_base64(data)

    fd = open('image.png', 'wb')
    fd.write(binary_data)
    fd.close()


    #file = io.BytesIO(urllib.urlopen(url).read())
    #im = Image.open('image.png')

    im = Image.open('image.png')
    im = im.resize((500, 500), Image.ANTIALIAS) #Could increase resolution which might improve accuracy
    image = np.reshape(np.array(im.getdata()).flatten(),(np.array(im.getdata()).flatten().shape[0],1))

    with open('Binary_model.pkl', 'rb') as fid:
        gnb_loaded = pickle.load(fid)

    prediction = gnb_loaded.predict(np.transpose(image))

    # return json
    return jsonify(dict([('class', prediction)]

if __name__ == "__main__":
    app.run()

#if __name__ == '__main__':
#    app.run(debug=True, host='localhost', port=5001) # http://localhost:5001/
#else:
#    application = app # for a WSGI server e.g.,
#    # twistd -n web --wsgi=hello_world.application --port tcp:5001:interface=localhost