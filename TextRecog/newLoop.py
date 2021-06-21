import glob
import os
from PIL import Image
import cv2
import easyocr
from PIL import Image, ImageEnhance

# Code to select recently arrived img in the folder
list_of_files = glob.glob('*.png') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

def sharpen():
    im = Image.open(latest_file)

    enhancer = ImageEnhance.Sharpness(im)
    factor = 9
    im_s_1 = enhancer.enhance(factor)
    im_s_1.save('sharpened-image.png')

# # AS IT IS Image
sharpen()
img=cv2.imread('sharpened-image.png' ,1)

rows,cols,ht=img.shape
#getRotationMatrix2D(Center,angle,scale)
matrix=cv2.getRotationMatrix2D((rows/2, cols/2),0,0.8)

new_img=cv2.warpAffine(img,matrix,(cols,rows))


cv2.imwrite('7.jpg',new_img)
i=0

rows,cols,ht=img.shape

#Using this loop to get INDIA P or SKF on the top side of bearing When we get it,Loop will break. 
while(i<12):    
    if i==0:
        matrix=cv2.getRotationMatrix2D((rows/2,cols/2),0,1)
        img=cv2.imread('7.jpg' ,1)


    else:
        matrix=cv2.getRotationMatrix2D((rows/2, cols/2),30,1)
        img=cv2.imread('7.jpg' ,1)

    new_img=cv2.warpAffine(img,matrix,(cols,rows))


    cv2.imwrite('7.jpg', new_img)

    reader=easyocr.Reader(['en'])

    result=reader.readtext('7.jpg',detail=0)
    print(result,"-----------------dfghjkfgyuguuhvhijh")
    i+=1
    if(result):
            
        if('INDIA' in result or 'india' in result or 'India' in result):    
            print("1111111111",result)
            break
        
        elif('SKF' in result or 'SkF' in result or 'skf' in result):    
            print("1111111111",result)
            break
        
    
    
    print(result)
    
print("END!@#$%^&*()__!@#$%^&*()_+",result)
  
#d is degree which we will use for rotating image.
#As we can see in image texts are located at 80-115 degrees from each other 
#so we are rotating image by specific  degrees (this may differ image to image) croping image and saving it to anather img and then reading text 
# To avoid blurring and for accuracy    
#Croping area may also differ 
d=(i-1)*30
i=0
img=cv2.imread('sharpened-image.png',1)
cv2.imwrite('7.jpg',img)

for i in range(8): 
    rows,cols,ht=img.shape

    matrix=cv2.getRotationMatrix2D((rows/2, cols/2),d,0.8)

    new_img=cv2.warpAffine(img,matrix,(cols,rows))


    cv2.imwrite('7.jpg', new_img)

    im = Image.open('7.jpg')
    # area variable contains parameters of the part of image which we are croping
    # (top,Left,Bottom,right,)
    #  (,Width,Height)
    area=(150,85,670,410)
    im1 = im.crop(area)
    im1.save('10.jpg')
                    
    reader=easyocr.Reader(['en'])

    a=reader.readtext('10.jpg',detail=0)
    result.append(a)
    d+=88
    print(result)
     
f=open("OP.txt", "w")
for i in result:
    f.write("%s\n" %i)
f.close()