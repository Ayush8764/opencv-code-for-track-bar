import cv2

def r(x):
    pass

img = cv2.imread('car.jpg')
cv2.namedWindow('Canny')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.createTrackbar('Thresh 1','Canny',0,255,r)
cv2.createTrackbar('Thresh 2','Canny',0,255,r)

while True:
    cv2.imshow('Original',img)
    key = cv2.waitKey(1)
    if key == 27:
        break
    t1 = cv2.getTrackbarPos('Thresh 1','Canny')
    t2 = cv2.getTrackbarPos('Thresh 2','Canny')
    
    canny_img = cv2.Canny(gray,t1,t2)
    cv2.imshow('Canny',canny_img)
    
cv2.destroyAllWindows()
