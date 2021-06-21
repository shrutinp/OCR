import easyocr
from PIL import Image
import cv2
reader = easyocr.Reader(['en'], gpu=False) 


# Original_Image = Image.open('7.png')
# print(Original_Image)
# cv2.imwrite('11.png',Original_Image)
# Original_Image=Original_Image.show()
# cv2.imwrite('11.png',Original_Image)

    
# def rotate():
# Giving The Orginal image Directory 
# Specified
# Original_Image = Image.open("7.png")
  
# Rotate Image By 180 Degree
# rotated_image1.show()
img=cv2.imread('5.jpg',1)
# rotated_image1 = img.rotate(-30)
# cv2.imwrite('8.png', rotated_image1)

# print(img)
rows,cols,ht=img.shape
# cv2.imshow('1', img)

matrix=cv2.getRotationMatrix2D((rows/2, cols/2),-4 ,1.1)

new_img=cv2.warpAffine(img,matrix,(cols,rows))

# cv2.imshow('2', new_img)

cv2.imwrite('7.jpg',new_img)
aa=Image.open('7.jpg')
area=(50,0,650,300)

a=aa.crop(area)

# cv2.imwrite('1.jpg',a)
a.save('1.jpg')
result = reader.readtext("1.jpg",detail = 0)
print(result)