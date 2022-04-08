import cv2 as cv

## converting a image into gray scale image 

img = cv.imread('Resources/Photos/cat.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('gray',gray)

#cv.waitKey(0)

## gray scale video 

# video = cv.VideoCapture('Resources/Videos/dog.mp4')

# while True:
#     istrue,frame = video.read()

#     gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

#     cv.imshow('gray',gray)

#     if cv.waitKey(20) and 0xFF == 'd':
#         break

# video.release()
# video.destroyAllWindows()

## Blur an image

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('park',img)
#cv.waitKey(0)
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT) ## this kernel size(ksize) needs to be tuple of odd numbers 

cv.imshow('blur',blur)
#cv.waitKey(0)


## edge detection 

## there are many methods to find the edges in the image, canny is a popular method/api  of opencv used to detect edges in a graph

img = cv.imread('Resources/Photos/park.jpg')
canny = cv.Canny(img,125,125)
cv.imshow('edges',canny)
#cv.waitKey(0)

img = cv.imread('Resources/Photos/cat.jpg')
canny = cv.Canny(img,125,125)
cv.imshow('edges',canny)
#cv.waitKey(0)


## to create a edge detection image of a image , if we take the blur image of the original image then the edge representation of blur image contain less edges and gives a better outline of the original image
img = cv.imread('Resources/Photos/park.jpg')
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
canny = cv.Canny(blur,125,125)
cv.imshow('edges',canny)
#cv.waitKey(0)

# Dilation is a technique where we expand the image. It adds the number of pixels to the boundaries of objects in an image 

# dilating a image 
img = cv.imread('Resources/Photos/park.jpg')
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
canny = cv.Canny(blur,125,125)
edges = cv.dilate(canny,(3,3),iterations=3)
cv.imshow('dilated_edges',edges)

# eroding is undilating an image 

## eroding a image 

erade = cv.erode(edges,(3,3),iterations=3)
cv.imshow('erades_edges',erade)

# resizing a image 

resize_image = cv.resize(img,(500,500)) #(500,500)->represents the dimension of resize image in terms of no. of pixels 

cv.imshow('resize_image',resize_image)

# crop image 

cropped_image = img[200:500,100:400]
cv.imshow('cropped image',cropped_image)

cv.waitKey(0)

