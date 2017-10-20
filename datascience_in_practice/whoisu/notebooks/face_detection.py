from PIL import Image
import numpy as np
import face_recognition as fr
#from keras.preprocessing.image import  array_to_img

def convert_to_face_only(ifile, ofile, final_height=120, final_width=120, raw_resize_fraction=0.5):
    try:
        image = fr.load_image_file(ifile)
        image = np.rot90(image,-1)
        face_locations = fr.face_locations(image)
        top,right,bottom,left = face_locations[0]
        face_image = image[top:bottom, left:right]
        small_img = Image.fromarray(face_image)
        small_img = small_img.resize((final_height, final_width))
        small_img.save(ofile)
    except Exception as e:
        print("WARNING: Can't detect face in {}! Skipping...".format(ifile), e)

