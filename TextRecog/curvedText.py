import cv2
import numpy as np
import easyocr

##(1) Read and resize the original image(too big)
img = cv2.imread("7.png")
# img1=PIL.Image.open("5.png")
# W,H=img1.size
# img = cv2.resize(img1, (W//4, H//4))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## (2) Detect circles
# circles = cv2.HoughCircles(gray, method=cv2.HOUGH_GRADIENT, dp=1, minDist=3, circles=None, param1=200, param2=100, minRadius = 200, maxRadius=0 )
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1.2, 2000) #


# cv2.imwrite("circles.png", cir)

## make canvas
canvas = img.copy()

## (3) Get the mean of centers and do offset
circles = np.int0(np.array(circles))
# cv2.imwrite("circles.png", circles)
x,y,r = 0,0,0
for ptx,pty, radius in circles[0]:
    cv2.circle(canvas, (ptx,pty), radius, (0,255,0), 1, 16)
    x += ptx
    y += pty
    r += radius

cnt = len(circles[0])
x = x//cnt
y = y//cnt
r = r//cnt 
x+=5
y-=7

## (4) Draw the labels in red
for r in range(100, r, 120):
    cv2.circle(canvas, (x,y), r, (0, 0, 255), 3, cv2.LINE_AA)
cv2.circle(canvas, (x,y), 3, (0,0,255), -1)

## (5) Crop the image
dr = r + 20
croped = img[y-dr:y+dr, x-dr:x+dr].copy()

## (6) logPolar and rotate
polar = cv2.logPolar(croped, (dr,dr),80, cv2.WARP_FILL_OUTLIERS )
rotated = cv2.rotate(polar, cv2.ROTATE_90_COUNTERCLOCKWISE)

## (7) Display the result
src_path=""
cv2.imshow("Canvas", canvas)
cv2.imshow("croped", croped)
cv2.imshow("polar", polar)
cv2.imshow("rotated", rotated)

## (8) Store rotated img    #SH
cv2.imwrite(src_path + "rotated.png", rotated)


## (9) Read image texts     #SH

reader = easyocr.Reader(['en'], gpu=False) 
result = reader.readtext('rotated.png',detail = 0)
print(result)
cv2.waitKey();cv2.destroyAllWindows()