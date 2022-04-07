import cv2 as cv 

def resize_image(frame,scale):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

if __name__=='__main__':
    img = cv.imread('Resources/Photos/cat_large.jpg')

    scale = 0.25 ## means 75% lesser than original

    resize_img = resize_image(img,scale)

    cv.imshow('resize_cat',resize_img)
    cv.waitKey(0)

    #--- for videos 

    video = cv.VideoCapture('Resources/Videos/dog.mp4')

    while True:
        istrue , frame = video.read()
        scale = 0.75
        frame = resize_image(frame,scale)
        cv.imshow('resize_dog_video',frame)

        if cv.waitKey(20) and 0xFF==ord('d'):
            break
    video.release()
    cv.destroyAllWindows()