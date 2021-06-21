# WORKING FINE
# READS TEXT FROM CROPED IMAGE.
# IMAGE SHARPENING CODE IS NOT INCLUDED
# CODE TO SELECT LATEST FILE IS INCLUDED
# Run code after particular time INCLUDED
import time
from PIL import Image
import cv2
import easyocr
import glob
import os


def readText():
    # # AS IT IS Image
    latest_file =LatestFile()
    img=cv2.imread(latest_file ,1)

    rows,cols,ht=img.shape
    # cv2.imshow('1', img)
    matrix=cv2.getRotationMatrix2D((rows/2, cols/2),0,0.8)

    new_img=cv2.warpAffine(img,matrix,(cols,rows))

    # cv2.imshow('2', new_img)

    cv2.imwrite('7.jpg',new_img)
        
        
    ## rotate till you get text on top of image
        
    i=0

    rows,cols,ht=img.shape

    while(i<12):    
        if i==0:
            matrix=cv2.getRotationMatrix2D((rows/2,cols/2),0,1)
            img=cv2.imread('7.jpg' ,1)


        else:
            matrix=cv2.getRotationMatrix2D((rows/2, cols/2),30,1)
            img=cv2.imread('7.jpg' ,1)

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
                
            if('INDIA' in result or 'india' in result or 'India' in result or 'INDIa' in result):    
                print("1111111111",result)
                break
            
            elif('SKF' in result or 'SkF' in result or 'skf' in result):    
                print("1111111111",result)
                break
            # d=i*10
            # matrix=cv2.getRotationMatrix2D((rows/2, cols/2),d,0.8)

            # new_img=cv2.warpAffine(img,matrix,(cols,rows) )

            # cv2.imshow('output', new_img)

            # cv2.imwrite('7.jpg', new_img)

            # im = Image.open('7.jpg')

            # # width, height = im.size

            # # Cropped image of below dimension
            # # area=(300,150,500,350)
            # area=(130,70,600,400)
            # im1 = im.crop(area)
            # im1.save('1.jpg')
                    
            # reader=easyocr.Reader(['en'])

            # result=reader.readtext('1.jpg',detail=0)
            # print(result)
            
        
        
        print(result)
        
    print("END!@#$%^&*()__!@#$%^&*()_+",result)
        
    d=(i-1)*30
    i=0
    img=cv2.imread('sharpened-image.png',1)
    cv2.imwrite('7.jpg',img)
    # rows,cols,ht=img.shape
    # while i<4:
        
    rows,cols,ht=img.shape

        # j=0
        # while j<=6:    
            # if(i==0):
                # rows,cols,ht=img.shape
            
        # matrix=cv2.getRotationMatrix2D((rows/2, cols/2),0,1)
        # img=cv2.imread('7.jpg' ,1)

        # new_img=cv2.warpAffine(img,matrix,(cols,rows))

        #         # cv2.imshow('output', new_img)

        # cv2.imwrite('7.jpg', new_img)

        # reader=easyocr.Reader(['en'])

        # result=reader.readtext('7.jpg',detail=0)


                
        #         # matrix=cv2.getRotationMatrix2D((rows/2, cols/2),-d,1)
        #         # new_img=cv2.warpAffine(img,matrix,(cols,rows))
        #         # result=reader.readtext('7.jpg',detail=0)
        #         # print("@#$%^&*(",result)
        # j+=1
        
            
        # rows,cols,ht=img.shape

    matrix=cv2.getRotationMatrix2D((rows/2, cols/2),-d,0.8)

    new_img=cv2.warpAffine(img,matrix,(cols,rows))

        # cv2.imshow('output', new_img)

    cv2.imwrite('7.jpg', new_img)

    im = Image.open('7.jpg')

            # width, height = im.size

            # Cropped image of below dimension
    area=(100,10,700,450)
    # area=(200,10,750,300)
    # area=(80,80,500,300)
    im1 = im.crop(area)
    im1.save('1.jpg')
                    
    reader=easyocr.Reader(['en'])

    a=reader.readtext('1.jpg',detail=0)
    result.append(a)
    print(result)
        
        # reader=easyocr.Reader(['en'])

        #         # if i%2==0:
        # result=reader.readtext('7.jpg',detail=0)
        # print("@#$%^&*(",result)
        # j+=1
                
    d+=90



    matrix=cv2.getRotationMatrix2D((rows/2, cols/2),-d,0.8)

    new_img=cv2.warpAffine(img,matrix,(cols,rows))

        # cv2.imshow('output', new_img)

    cv2.imwrite('7.jpg', new_img)

    im = Image.open('7.jpg')

            # width, height = im.size

            # Cropped image of below dimension
    area=(100,50,700,400)
    # area=(100,150,800,500)
    # area=(200,10,750,300)
    # area=(80,80,500,300)
    im1 = im.crop(area)
    im1.save('2.jpg')
                    
    reader=easyocr.Reader(['en'])

    a=reader.readtext('2.jpg',detail=0)
    result.append(a)
    print(result)


    d+=90


    matrix=cv2.getRotationMatrix2D((rows/2, cols/2),-d,0.8)

    new_img=cv2.warpAffine(img,matrix,(cols,rows))

        # cv2.imshow('output', new_img)

    cv2.imwrite('7.jpg', new_img)

    im = Image.open('7.jpg')

            # width, height = im.size

            # Cropped image of below dimension
    area=(100,50,700,350)
    # area=(200,10,750,300)
    # area=(80,80,500,300)
    im1 = im.crop(area)
    im1.save('3.jpg')
                    
    reader=easyocr.Reader(['en'])

    a=reader.readtext('3.jpg',detail=0)
    result.append(a)
    print(result)


    d+=90

    matrix=cv2.getRotationMatrix2D((rows/2, cols/2),-d,0.8)

    new_img=cv2.warpAffine(img,matrix,(cols,rows))

        # cv2.imshow('output', new_img)

    cv2.imwrite('7.jpg', new_img)

    im = Image.open('7.jpg')

            # width, height = im.size
    
            # Cropped image of below dimension
            # area=(300,150,500,350)
    # area=(200,10,750,300)
    area=(100,80,650,400)
    im1 = im.crop(area)
    im1.save('4.jpg')
                    
    reader=easyocr.Reader(['en'])

    a=reader.readtext('4.jpg',detail=0)
    result.append(a)
    print(result)

    d+=90



    matrix=cv2.getRotationMatrix2D((rows/2, cols/2),-d,0.8)

    new_img=cv2.warpAffine(img,matrix,(cols,rows))

        # cv2.imshow('output', new_img)

    cv2.imwrite('7.jpg', new_img)

    im = Image.open('7.jpg')

            # width, height = im.size

            # Cropped image of below dimension
    area=(200,50,550,450)
    # area=(200,10,550,300)
    # area=(80,80,500,300)
    im1 = im.crop(area)
    im1.save('5.jpg')
                    
    reader=easyocr.Reader(['en'])

    a=reader.readtext('5.jpg',detail=0)
    result.append(a)
    print(result)

    d+=90



    matrix=cv2.getRotationMatrix2D((rows/2, cols/2),-d,0.8)

    new_img=cv2.warpAffine(img,matrix,(cols,rows))

        # cv2.imshow('output', new_img)

    cv2.imwrite('7.jpg', new_img)

    im = Image.open('7.jpg')

            # width, height = im.size

            # Cropped image of below dimension
            # area=(300,150,500,350)
    # area=(200,10,750,300)
    area=(300,150,800,400)
    # area=(80,80,500,300)
    im1 = im.crop(area)
    im1.save('6.jpg')
                    
    reader=easyocr.Reader(['en'])

    a=reader.readtext('6.jpg',detail=0)
    result.append(a)
    print(result)


    d+=85


    matrix=cv2.getRotationMatrix2D((rows/2, cols/2),-d,0.8)

    new_img=cv2.warpAffine(img,matrix,(cols,rows))

        # cv2.imshow('output', new_img)

    cv2.imwrite('7.jpg', new_img)

    im = Image.open('7.jpg')

            # width, height = im.size

            # Cropped image of below dimension
    area=(150,100,650,450)
    # area=(50,50,600,500)
    # area=(200,10,750,300)
    im1 = im.crop(area)
    im1.save('8.jpg')
                    
    reader=easyocr.Reader(['en'])

    a=reader.readtext('8.jpg',detail=0)
    result.append(a)
    print(result)


    d+=90

    matrix=cv2.getRotationMatrix2D((rows/2, cols/2),-d,0.8)

    new_img=cv2.warpAffine(img,matrix,(cols,rows))

        # cv2.imshow('output', new_img)

    cv2.imwrite('7.jpg', new_img)

    im = Image.open('7.jpg')

            # width, height = im.size

            # Cropped image of below dimension
            # area=(300,150,500,350)
    area=(150,100,650,380)
    im1 = im.crop(area)
    im1.save('9.jpg')
                    
    reader=easyocr.Reader(['en'])

    a=reader.readtext('9.jpg',detail=0)
    result.append(a)
    print(result)
    
    Save(result)

def Save(result):
    f=open("OP.txt", "w")
    for i in result:
        if(i):
            f.write("%s\n" %i)
    f.close()

# Code to select recently arrived img in the folder
def LatestFile():
    list_of_files = glob.glob('*.png') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    return latest_file

while 1:
    readText()
    time.sleep(30)

