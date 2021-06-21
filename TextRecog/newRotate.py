# WORKING FINE
# READS TEXT FROM CROPED IMAGE.
#IMAGE SHARPENING CODE IS INCLUDED
#+ or - direction is included 

from PIL import Image, ImageEnhance
import cv2
import easyocr


# This function sharpens code by some factor
def sharp():
    im = Image.open("img/6666.png") #image sharpening is PIL function so we have to use  Image.open(path)

    enhancer = ImageEnhance.Sharpness(im)

    factor = 9
    im_s_1 = enhancer.enhance(factor)
    # saving image stored in variable "im_s_1" into "sharpened-image.png"
    im_s_1.save('sharpened-image.png')

# 
sharp()
img=cv2.imread('sharpened-image.png' ,1) #Rotation is OpenCV library function so we are reading the image

rows,cols,ht=img.shape 
# We can access height, width and number of channels 
# from img.shape: Height is at index 0, 
# Width is at index 1; 
# and number of channels at index 2 (Number of Channels represents the number of components used to represent each pixel.)

# cv2.imshow('1', img)

matrix=cv2.getRotationMatrix2D((rows/2, cols/2),0,0.8) #getRotationMatrix2d(centre,RotationAngle,Scale)

new_img=cv2.warpAffine(img,matrix,(cols,rows))
# rotated image is stored in new_img

cv2.imwrite('7.jpg',new_img)
    

## rotate till you get text i.e INDIA P OR SKF on top of image
    
# result=['INDIA P']
# print(result,"345678=86")
i=0

rows,cols,ht=img.shape

# below code is used to know in which direction we should rotate + or -
j=0
flag=0
while(i<4):    
    # result=''
    # print(result[0])
    
    # cv2.imshow('new', new_img)
    # cv2.imshow('img',img)
    if i==0:
        matrix=cv2.getRotationMatrix2D((rows/2,cols/2),0,1)
        img=cv2.imread('7.jpg' ,1)
            
    # Check in which direction you should rotate (+ or -) 
    # j=0
    # here we are rotating 120 deg in + direction .
    # if we get text we will come out of loop 
    # else we will raotate in -ve direction
    while j<=4:
        matrix=cv2.getRotationMatrix2D((rows/2, cols/2),30,1)
        img=cv2.imread('7.jpg' ,1)
        j+=1
        new_img=cv2.warpAffine(img,matrix,(cols,rows))

        # cv2.imshow('output', new_img)

        cv2.imwrite('7.jpg', new_img)

        reader=easyocr.Reader(['en'])

        result=reader.readtext('7.jpg',detail=0)
        print(result,"-----------------dfghjkfgyuguuhvhijh")
        # cv2.imshow('output', new_img)
        i+=1
        if(result):
            # if(result[0] or result[1] or result[2] or result[3]=='INDIA P' or result[0] or result[1] or result[2] or result[3]=='Indiap' or result[0] or result[1] or result[2] or result[3]=='IndiaP' or result[0] or result[1] or result[2] or result[3]=='INDIAP' or result[0] or result[1] or result[2] or result[3]=='InDiap' or result[0] or result[1] or result[2] or result[3]=='InDiaP' or result[0] or result[1] or result[2] or result[3]=='India' or result[0]=='India' or result[0]=='IndiaP' or result[0]=='INDIA'):
                
            if('INDIA' in result or 'india' in result or 'India' in result):    
                print("1111111111",result)
                flag=1
                break
            
            elif('SKF' in result or 'SkF' in result or 'skf' in result):    
                print("1111111111",result)
                flag=1
                break
    # REading the same image again so that text will come at original position
    
    if(flag==1):
        break
    while j>4 and j<8 :
        if(j==5):
            img=cv2.imread('sharpened-image.png' ,1)
            cv2.imwrite('7.jpg',img)

        matrix=cv2.getRotationMatrix2D((rows/2, cols/2),-30,1)
        img=cv2.imread('7.jpg' ,1)
        j+=1
        new_img=cv2.warpAffine(img,matrix,(cols,rows))

    # cv2.imshow('output', new_img)

        cv2.imwrite('7.jpg', new_img)

        reader=easyocr.Reader(['en'])

        result=reader.readtext('7.jpg',detail=0)
        print(result,"-----------------dfghjkfgyuguuhvhijh")
        # cv2.imshow('output', new_img)
        i+=1
        if(result):
            # if(result[0] or result[1] or result[2] or result[3]=='INDIA P' or result[0] or result[1] or result[2] or result[3]=='Indiap' or result[0] or result[1] or result[2] or result[3]=='IndiaP' or result[0] or result[1] or result[2] or result[3]=='INDIAP' or result[0] or result[1] or result[2] or result[3]=='InDiap' or result[0] or result[1] or result[2] or result[3]=='InDiaP' or result[0] or result[1] or result[2] or result[3]=='India' or result[0]=='India' or result[0]=='IndiaP' or result[0]=='INDIA'):
                
            if('INDIA' in result or 'india' in result or 'India' in result):    
                print("1111111111",result)
                break
            
            elif('SKF' in result or 'SkF' in result or 'skf' in result):    
                print("1111111111",result)
                break
    print('SHRUTI',result)
    
print("END!@#$%^&*()__!@#$%^&*()_+",result)
print(j,"JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJj")
'''
below 8 lines of code is to determine in which direction image should rotate
'''
x=0
if(j<=4):
    d=(j-1)*30
    x=1
else:
    d=(j-1)*-30
    x=-1
i=0
print(x)


img=cv2.imread('sharpened-image.png',1)
cv2.imwrite('7.jpg',img)
    
rows,cols,ht=img.shape
matrix=cv2.getRotationMatrix2D((rows/2, cols/2),(d*x),0.8)
new_img=cv2.warpAffine(img,matrix,(cols,rows))

cv2.imwrite('7.jpg', new_img)
im = Image.open('7.jpg')
area=(100,10,700,450)
im1 = im.crop(area)
im1.save('1.jpg')
                
reader=easyocr.Reader(['en'])
result=reader.readtext('1.jpg',detail=0)
print(result)
     
            
d+=90

matrix=cv2.getRotationMatrix2D((rows/2, cols/2),(d*x),0.8)
new_img=cv2.warpAffine(img,matrix,(cols,rows))

cv2.imwrite('7.jpg', new_img)
im = Image.open('7.jpg')
area=(100,50,700,400)
im1 = im.crop(area)
im1.save('2.jpg')
                
reader=easyocr.Reader(['en'])
a=reader.readtext('2.jpg',detail=0)
result.append(a)
print(result)


d+=90

matrix=cv2.getRotationMatrix2D((rows/2, cols/2),(d*x),0.8)
new_img=cv2.warpAffine(img,matrix,(cols,rows))

cv2.imwrite('7.jpg', new_img)
im = Image.open('7.jpg')
area=(100,50,700,350)
im1 = im.crop(area)
im1.save('3.jpg')
                
reader=easyocr.Reader(['en'])
a=reader.readtext('3.jpg',detail=0)
result.append(a)
print(result)


d+=90

matrix=cv2.getRotationMatrix2D((rows/2, cols/2),(d*x),0.8)
new_img=cv2.warpAffine(img,matrix,(cols,rows))

cv2.imwrite('7.jpg', new_img)
im = Image.open('7.jpg')
area=(150,10,600,500)
im1 = im.crop(area)
im1.save('4.jpg')

reader=easyocr.Reader(['en'])
a=reader.readtext('4.jpg',detail=0)
result.append(a)
print(result)


d+=90

matrix=cv2.getRotationMatrix2D((rows/2, cols/2),(d*x),0.8)
new_img=cv2.warpAffine(img,matrix,(cols,rows))

cv2.imwrite('7.jpg', new_img)
im = Image.open('7.jpg')
area=(200,50,550,450)
im1 = im.crop(area)
im1.save('5.jpg')
                
reader=easyocr.Reader(['en'])
a=reader.readtext('5.jpg',detail=0)
result.append(a)
print(result)


d+=90

matrix=cv2.getRotationMatrix2D((rows/2, cols/2),(d*x),0.8)
new_img=cv2.warpAffine(img,matrix,(cols,rows))

cv2.imwrite('7.jpg', new_img)
im = Image.open('7.jpg')
area=(150,10,650,450)
im1 = im.crop(area)
im1.save('6.jpg')
                
reader=easyocr.Reader(['en'])
a=reader.readtext('6.jpg',detail=0)
result.append(a)
print(result)


d+=90

matrix=cv2.getRotationMatrix2D((rows/2, cols/2),(d*x),0.8)
new_img=cv2.warpAffine(img,matrix,(cols,rows))

cv2.imwrite('7.jpg', new_img)
im = Image.open('7.jpg')
area=(400,250,700,350)
im1 = im.crop(area)
im1.save('8.jpg')
                
reader=easyocr.Reader(['en'])
a=reader.readtext('8.jpg',detail=0)
result.append(a)
print(result)


d+=90

matrix=cv2.getRotationMatrix2D((rows/2, cols/2),(d*x),0.8)
new_img=cv2.warpAffine(img,matrix,(cols,rows))

cv2.imwrite('7.jpg', new_img)
im = Image.open('7.jpg')
area=(150,10,650,450)
im1 = im.crop(area)
im1.save('9.jpg')
                
reader=easyocr.Reader(['en'])
a=reader.readtext('9.jpg',detail=0)
result.append(a)
print(result)


f=open("OP.txt","w")    
for i in result:
        f.write("%s\n" %i)
f.close()
    