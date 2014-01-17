#!/usr/bin/env python
import cv2
import numpy as np
from random import randint

# Region of interest
class Roi(object):
	roiCount = 0	# static Roi counter used as id
	def __init__(self, x1, x2, y1, y2, color = None, id = None, label = None):
		self.label = label or None
		self.id = id or self.__class__.roiCount
		self.__class__.roiCount += 1
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.color = color or [randint(1,254),randint(1,254),randint(1,254)] # white rgb
		self.intensity = 0
		self.mask = np.zeros((480,640), np.uint8)
		for row in xrange(self.y1,self.y2):
			for col in xrange(self.x1,self.x2):
				self.mask[row][col] = 1

	# Calculates color intensity in a region of interest
	def calculateIntensity(self,image):
		intensity = cv2.mean(np.int32(image), mask=self.mask)
		# for row in xrange(self.y1, self.y2):
		# 	for col in xrange(self.x1, self.x2):
		# 		intensity += image[row][col]
		return intensity

	# Updates Roi
	def update(self, image):
		self.intensity = self.calculateIntensity(image)
		return self.intensity

# Button: adds team to sorted (intensity-descending) teams list
def addTeam(x1, x2, y1, y2, color = None, id = None, label = None):
	t = Roi(x1, x2, y1, y2, color, id, label)
	if len(teams) <= 0:
		teams.append(t)
	else:
		for i in xrange(len(teams)):
			print teams[i].intensity, "t: ", t.intensity
			if teams[i].intensity < t.intensity:
				teams.insert(i,t) # prepend
				return t.id
		teams.append(t)
	return t.id

# Button: remove team from teams
def removeTeam(id):
	for t in teams:
		if t.id == id:
			teams.remove(t)

def removeAll():
	teams = []

def sortTeams():
	teams.sort(key=lambda t: t.intensity, reverse=True)

# Get an image (stream) to display
def getImage():
	image = [[1,2,3,4,5],[1,2,3,4,5]] # 2 dimensional grayscale image
	return image

# Update all teams with one image
def updateAll(image):
	for t in teams:
		t.update(image)

# Creates a rectangular border mask from given params
def createBorderMask(img, x,x2,y,y2, color = None, borderWidth = None):
	color = color or 255
	borderWidth = borderWidth or 10
	h = y2 - y
	w = x2 - x
	mask = np.zeros(img.shape[:2],np.uint8)
	mask[y:y+borderWidth,x:x+w] = color		# top
	mask[y+h:y+h+borderWidth,x:x+w+borderWidth] = color	# bottom
	mask[y:y+h,x:x+borderWidth] = color		# left
	mask[y:y+h,x+w:x+w+borderWidth] = color	# right 
	return mask


teams = []			# List of teams



