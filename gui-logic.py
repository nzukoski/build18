#!/usr/bin/env python

import cv2
import numpy as np

def logic(coords):
	pass


def getImage():
	c = cv2.VideoCapture(0)
	_,f = c.read()
	y1 = 0
	y2 = 100
	x1 = 0
	x2 = 100
	mask = np.zeros(f.shape, dtype=np.uint8)
	roi_corners = np.array([[(10,10), (300,300), (10,300)]], dtype=np.int32)
	white = (255, 255, 255)
	cv2.fillPoly(mask, roi_corners, white)

	# masked_image = cv2.bitwise_and(f, mask)

	masked_image = cv2.mean(f, mask)
	# masked_image = cv2.mean(f, roi_corners)
	
	cv2.imshow('masked image', masked_image)
	cv2.waitKey()
	cv2.destroyAllWindows()
	c.release()
	# old_roi = cvGetImageROI(img); 
	# cvSetImageROI(img, cvRect(x,y,width,height)); 
	# CvScalar c = cvAvg(img); 
	# cvSetImageROI(img,old_roi); // reset old roi 
	# cv2.cv.SetImageROI

getImage()

