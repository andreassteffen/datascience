from PIL import Image,PILImage
import numpy as np
import cv2
import face_recognition as fr
#from keras.preprocessing.image import  array_to_img

def cast_opencv_array_to_numpy(x):
    return np.swapaxes(x, 0,1)

def __get_face(imagePath,final_width=120, final_height=120):
    """
    This function returns a numpy array representation of the detected face in the image imagePath.
    """
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    #faces = faceCascade.detectMultiScale(gray, 1.2, 5)
    print("Found {} faces in {}".format(len(faces), imagePath))
    im = Image.open(imagePath)
    try:
        (x, y, w, h) = faces[-1]
        center_x = x+w/2
        center_y = y+h/2
        b_dim = min(max(w,h)*1.2,im.width, im.height) # WARNING : this formula in incorrect
        #box = (x, y, x+w, y+h)
        box = (center_x-b_dim/2, center_y-b_dim/2, center_x+b_dim/2, center_y+b_dim/2)
        # Crop Image
        crpim = im.crop(box).resize((final_width,final_height))
        #return cast_opencv_array_to_numpy(np.asarray(crpim)[:,:,:3]) #fourth channel is transparency
        return cast_opencv_array_to_numpy(np.asarray(crpim)) #fourth channel is transparency

    except:
        return None
        
def convert_to_face_only_haar(ifile, ofile,final_width=120, final_height=120):
    img_ar = __get_face(ifile,final_width=120, final_height=120)
    if img_ar is not None:
        img = Image.fromarray(img_ar) 
        img.save(ofile)
    else:
       "WARNING: Can't detect face in {}! Skipping...".format(ifile)

def convert_to_face_only(ifile, ofile, final_width=120, final_width=120, raw_resize_fraction=0.5):
    try:
        image = fr.load_image_file(ifile)
        image = np.rot90(image,-1)
        face_locations = fr.face_locations(image)
        top,right,bottom,left = face_locations[0]
        face_image = image[top:bottom, left:right]
        small_img = PILImage.fromarray(face_image)
        small_img = small_img.resize((final_height, final_width))
        small_img.save(ofile)
    except:
       "WARNING: Can't detect face in {}! Skipping...".format(ifile)

