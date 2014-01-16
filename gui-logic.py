#!/usr/bin/env python

import cv2

def logic(coords):
	pass

# Region of interest
class Roi(object):
	def __init__(self, image, x1, x2, y1, y2):
		self.image = image
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.update()

	# Calculates color intensity in a region of interest
	def calculateIntensity(self):
		intensity = 0
		for row in xrange(self.y1,self.y2):
			for col in xrange(self.x1,self.x2):
				intensity += self.image[row][col]
		return intensity

	# Updates Roi
	def update(self):
		self.intensity = self.calculateIntensity()
		return self.intensity


def getImage():
	image = [[1,2,3,4,5],[1,2,3,4,5]] # 2 dimensional grayscale image
	return image

image = getImage()
team1 = Roi(image,0,3,0,1)	# teams

print team1.update()	# gets intensity (also team1.intensity)


