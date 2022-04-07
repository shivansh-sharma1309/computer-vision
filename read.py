import cv2 as cv
# # imread is used to read image and return a matrix of pixel values
img = cv.imread('Resources/Photos/cat_large.jpg')
# # imshow is used to display the image matrix
cv.imshow('cat',img)
# # waitKey allows users to display a window for given milliseconds or until any key is pressed. It takes time in milliseconds as a parameter and waits for the given time to destroy the window, if 0 is passed in the argument it waits till any key is pressed.
cv.waitKey(0)

# cv.videoCapture is used to capture a video , 0 is used to represent a web cam , if we have saved video then we need to pass the path of that video 

#displaying videos
# for web cam capture = cv.VideoCapture(0)
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True :
    istrue , frame = capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.detroyAllWindows()