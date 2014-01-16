#!/usr/bin/env python

# Region of interest
class Roi(object):
	roiCount = 0	# static Roi counter used as id
	def __init__(self, image, x1, x2, y1, y2, id = None):
		self.id = id or self.__class__.roiCount
		self.__class__.roiCount += 1
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

# Button: adds team to teams list
def addTeam(image, x1, x2, y1, y2, id = None):
	t = Roi(image, x1, x2, y1, y2, id)
	teams.append(t)

# Button: remove team from teams
def removeTeam(id):
	for t in teams:
		if t.id == id:
			teams.remove(t)

# Get an image (stream) to display
def getImage():
	image = [[1,2,3,4,5],[1,2,3,4,5]] # 2 dimensional grayscale image
	return image

image = getImage()
teams = []

for i in xrange(3):
	addTeam(image,0,3,0,1)	# teams
	print teams[i].id


