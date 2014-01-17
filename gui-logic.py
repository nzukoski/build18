#!/usr/bin/env python

# Region of interest
class Roi(object):
	roiCount = 0	# static Roi counter used as id
	def __init__(self, x1, x2, y1, y2, id = None):
		self.id = id or self.__class__.roiCount
		self.__class__.roiCount += 1
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2

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
def addTeam(image, x1, x2, y1, y2, id = None):
	t = Roi(image, x1, x2, y1, y2, id)
	if len(teams) <= 0:
		teams.append(t)
	else:
		for i in xrange(len(teams)):
			if teams[i].intensity < t.intensity:
				teams.insert(i,t) # prepend
				return
		teams.append(t)

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


# ---------------------- Logic goes here ---------------------------------
image = getImage()	# Pass in or get an image to work with
teams = []			# List of teams


addTeam(image,0,2,0,1)	# teams
addTeam(image,0,1,0,1)	# teams
addTeam(image,0,3,0,1)	# teams

sortTeams()

for i in xrange(3):
	print teams[i].id," ", teams[i].intensity


