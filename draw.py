import cv2 as cv 
import numpy as np

# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('cat',img)

# ---- create a blank image 

black_img = np.zeros((500,500,3),dtype='uint8') # (500,500,3) -> here 3 represents color channels in image which are in this case is 3 i.e. red,green,blue;

# paint image with a specific color

black_img[:] = 0,255,0 

# draw a rectangle , circle,line
black_img[:] = 0,0,0
cv.rectangle(black_img,(0,0),(255,255),(0,255,0),thickness = 2)
cv.imshow('grenn',black_img)
cv.waitKey(0)
cv.circle(img = black_img,center = (285,285),radius = 40,color = (0,0,255),thickness = cv.FILLED) #thickness = cv.FILLED or -1
cv.imshow('circle',black_img)
cv.waitKey(0)
cv.line(black_img,(0,0),(255,255),(255,255,255),thickness = 2)
cv.imshow('line',black_img)
cv.waitKey(0)

# text on an image

cv.putText(black_img,'SHiVANSH SHARMA',(120,255),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,1.0,(255,130,218))
cv.imshow('text',black_img)
cv.waitKey(0)