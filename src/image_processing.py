import cv2
import numpy as np

"""
def image_BnW(series_value, path):
    im = cv2.imread(f"{path}/{series_value}")    
    return cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
"""

def colorImage(series_value, path, debug):
    im = cv2.imread(f"{path}/{series_value}")  
    if debug:
        return cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    return cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

def sizeImage(series_value, size):
    print("inter_cubic")
    return cv2.resize(series_value, size, interpolation=cv2.INTER_CUBIC) 

def normalizeImage(series_value):
    return series_value/np.amax(series_value) 

def imageDenoiseMEdianBlur(series_value, ksize):
    return cv2.medianBlur(series_value, ksize)

def imageDenoiseBlur(series_value, ksize):
    return cv2.blur(series_value, ksize)


