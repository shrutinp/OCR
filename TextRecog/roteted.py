# WORKING FINE
# READS TEXT FROM IMAGE WHILE ROTATING . DOESNT CROP IMAGE


from PIL import Image
import cv2
import easyocr
import numpy
# AS IT IS Image
img=cv2.imread('img/66q.png' ,1)


rows,cols,ht=img.shape

matrix=cv2.getRotationMatrix2D((rows/2, cols/2),30,0.8)

new_img=cv2.warpAffine(img,matrix,(cols,rows) )

cv2.imshow('output', new_img)

cv2.imwrite('7.jpg', new_img)


im = Image.open('7.jpg')

# width, height = im.size

# Cropped image of below dimension
area=(300,150,500,350)
# area=(130,70,600,400)
im1 = im.crop(area)
im1.save('1.jpg')



reader=easyocr.Reader(['en'])

result=reader.readtext('1.jpg',detail=0)
print(result)
   
   
# # AS IT IS Image
# img=cv2.imread('66q.png' ,1)

# rows,cols,ht=img.shape
# # im = Image.fromarray(numpy.uint8(img))

# matrix=cv2.getRotationMatrix2D((rows/2, cols/2),-30,0.8)
# # new_img=img.rotate(90, resample=Image.BICUBIC, expand=True)


# new_img=cv2.warpAffine(img,matrix,(cols,rows) )

# cv2.imshow('output', new_img)

# # new_img.save('7.jpg', new_img)

# reader=easyocr.Reader(['en'])

# result=reader.readtext('7.jpg',detail=0)
# print(result) 

# img=cv2.imread('66q.png' ,1)
# cv2.imwrite('7.jpg',img)

d=30
i=0
while i<8:

    d+=90
    
    rows,cols,ht=img.shape

    matrix=cv2.getRotationMatrix2D((rows/2, cols/2),-d,0.8)

    new_img=cv2.warpAffine(img,matrix,(cols,rows) )

    # cv2.imshow('output', new_img)

    cv2.imwrite('7.jpg', new_img)

    reader=easyocr.Reader(['en'])

    result=reader.readtext('7.jpg',detail=0)
    print(result)
    i+=1
