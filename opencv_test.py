# import numpy as np
# import cv2 as cv2

# img1 = cv2.imread("img1.jpeg")
# img2 = cv2.imread("img2.jpeg")

# diffImg = cv2.absdiff(img1, img2)
# absDiff = cv2.cvtColor(diffImg, cv2.COLOR_BGR2GRAY)
# retval, threshold = cv2.threshold(absDiff, 127, 255, cv2.THRESH_BINARY)
# #print retval
# #cv2.imshow('img2', absDiff)
# #cv2.imshow('img4', threshold)
# #cv2.waitKey()

# #cv2.destroyAllWindows()

import cv2
import numpy as np
 
c = cv2.VideoCapture(0)
_,f = c.read()
 
avg1 = np.float32(f)
avg2 = np.float32(f)
print f.shape
heatmap = np.zeros((480,640), np.uint8)
 
while(1):
    _,f = c.read()
    converted_f = np.float32(f)
    diffImage = cv2.subtract(avg1, converted_f)
    #diffImage = cv2.absdiff(avg1, converted_f)
    absDiff = cv2.cvtColor(diffImage, cv2.COLOR_BGR2GRAY)
    retval, threshold = cv2.threshold(absDiff, 65, 1, cv2.THRESH_BINARY)
    heatmap += threshold
    cv2.accumulateWeighted(f,avg1,0.1)
     
    res1 = cv2.convertScaleAbs(avg1)
 
    cv2.imshow('img',f)
    cv2.imshow('avg1',res1)
    cv2.imshow('threshold', threshold * 255)
    cv2.imshow('heatmap', heatmap)
    k = cv2.waitKey(20)
 
    if k == 27:
        break
 
cv2.destroyAllWindows()
c.release()

