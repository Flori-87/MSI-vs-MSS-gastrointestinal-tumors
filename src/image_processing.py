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

