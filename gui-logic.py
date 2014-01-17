#!/usr/bin/env python

import cv2
import numpy as np

# Region of interest
class Roi(object):
	roiCount = 0	# static Roi counter used as id
	def __init__(self, x1, x2, y1, y2, color = None, id = None):
		self.id = id or self.__class__.roiCount
		self.__class__.roiCount += 1
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.color = color or [255,255,255] # white rgb
		self.intensity = 0

	# Calculates color intensity in a region of interest
	def calculateIntensity(self,image):
		intensity = 0
		for row in xrange(self.y1,self.y2):
			for col in xrange(self.x1,self.x2):
				intensity += image[row][col]
		return intensity

	# Updates Roi
	def update(self, image):
		self.intensity = self.calculateIntensity(image)
		return self.intensity

# Button: adds team to sorted (intensity-descending) teams list
def addTeam(x1, x2, y1, y2, color = None, id = None):
	t = Roi(x1, x2, y1, y2, color, id)
	if len(teams) <= 0:
		teams.append(t)
	else:
		for i in xrange(len(teams)):
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
def createRectMask(img, x,x2,y,y2, color = None, borderWith = None):
	color = color or 255
	borderWith = borderWidth or 10
	h = y2 - y
	w = x2 - x
	mask = np.zeros(img.shape[:2],np.uint8)
	mask[y:y+borderWith,x:x+w] = color		# top
	mask[y+h:y+h+borderWith,x:x+w+borderWith] = color	# bottom
	mask[y:y+h,x:x+borderWith] = color		# left
	mask[y:y+h,x+w:x+w+borderWith] = color	# right 
	return mask



# ---------------------- Logic goes here ---------------------------------
image = getImage()	# Pass in or get an image to work with
teams = []			# List of teams


addTeam(0,2,0,1, [100,100,100])	# teams
addTeam(0,1,0,1, [150,150,150])	# teams
tId = addTeam(0,3,0,1)	# teams

removeTeam(tId)	# remove a team

updateAll(image)
sortTeams()

for i in xrange(len(teams)):
	print teams[i].id," ", teams[i].intensity






