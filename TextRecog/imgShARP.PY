'''
For Image sharpening

use PIL functions for reading and saving image
'''
from PIL import Image, ImageEnhance

im = Image.open("img/6666.png")

enhancer = ImageEnhance.Sharpness(im)

factor = 9 
im_s_1 = enhancer.enhance(factor)
im_s_1.save('3.jpg')