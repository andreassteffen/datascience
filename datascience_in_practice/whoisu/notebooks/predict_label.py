#!/usr/bin/env python
import numpy as np
import pickle 
from keras.models import load_model
from keras.preprocessing.image import  img_to_array, load_img
import face_recognition as fr
from PIL import Image

class Predictor:
    def __init__(self, kerasmodelfile):
        self.kerasmodelfile = kerasmodelfile
        self.picklefile = kerasmodelfile.replace("h5", "pickle")
        self.model = load_model(self.kerasmodelfile)
        with open(self.picklefile, 'rb') as handle:
            self.ids_to_classes = pickle.load(handle)
    
    def convert_to_face_only(self, ifile, final_height=120, final_width=120, raw_resize_fraction=0.5):
        image = fr.load_image_file(ifile)
        image = np.rot90(image,-1)
        face_locations = fr.face_locations(image)
        top,right,bottom,left = face_locations[0]
        face_image = image[top:bottom, left:right]
        small_img = Image.fromarray(face_image)
        small_img = small_img.resize((final_height, final_width))
        return np.array(small_img)[:,:,:3]

    def predict(self, imagefn):
        x = self.convert_to_face_only(imagefn)
        x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)
        x /= 255.
        prob = self.model.predict(x)
        #print(prob,np.argmax(prob),len(ids_to_classes))
        return self.ids_to_classes[np.argmax(prob)]
#def predict(imagefn, kerasmodelfile, picklefile):
#    model = load_model(kerasmodelfile)
#    with open(picklefile, 'rb') as handle:
#        ids_to_classes = pickle.load(handle)
#    img = load_img(imagefn)  # this is a PIL image    
#    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
#    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)
#    prob = model.predict(x)
#    print(prob,np.argmax(prob),len(ids_to_classes))

