'''
    This file contains code for 
    Croping image using image. Crop(area)
    Crop function is function from PIL library. And we should use save() for saving image
'''

# Improting Image class from PIL module
from PIL import Image
import cv2
import easyocr
import numpy
# Opens a image in RGB mode

im = Image.open('66q.png')
img=cv2.imread('66q.png')

# Size of the image in pixels (size of orginal image)
# (This is not mandatory)
width, height = im.size


# Crop  ped image of below dimension
# (It will not change orginal image)
area=(100,100,650,250)
im1 = im.crop(area)
im1.save('1.jpg')
im1=cv2.imread('1.jpg')
reader = easyocr.Reader(['en'], gpu=False) 

result = reader.readtext('1.jpg',detail = 0)

print("Original Croped",result)
