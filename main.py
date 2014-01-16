#!/usr/bin/env python
import cv2
import numpy as np
from fabric.api import *
from time import sleep


# globals 
env.user = "pi"
env.password = "build18"
remoteHosts = ["128.237.241.93"]
avg = np.float32(cv2.imread("temp.jpeg"))

# Holds info on running average (delta heat map) of images
class Average(object):
	def __init__(self, image = None):
		self.image = image or None
	def update(self, newImage):
		# find new running average
		self.image -= newImage # not like this


# Run a command on remote host
def runCommand(command, host):
    print "Command: " + command + " || Host: " + host
    env.host_string = host
    picId = str(run(command))
    return picId

# Get a file from a remote host
def getFile(remotePath, localPath, host):
	env.host_string = host
	pic = get(remotePath, localPath)
	return pic

# Display image on screen
def display(image):
	# output the image to the screen/update current
	pass

# Stitch images together using magic
def stitchImages(images):
	#magic
	return image

# Main loop polls raspi's for images and processes running average
def main():
	average = Average()
	while(True):
		images = []
		for host in remoteHosts:	# get new images
			try:
				with cd('~/build18/images'):
					picPath = runCommand("/home/pi/build18/images/updatelatest.sh", host)
					print picPath
					pic = getFile(picPath, "~/roomal/build18/temp.jpeg", host)
			except:
				print "Error with ssh"
		# stitch images
		print 
		newImage = cv2.imread("temp.jpeg")

		cv2.accumulateWeighted(newImage, avg, 0.1)

		res = cv2.convertScaleAbs(avg)
		cv2.imshow('img', newImage)
		cv2.imshow('avg', res)
		k = cv2.waitKey(10)
 		
		if k == 27:
			break

main()
cv2.destroyAllWindows()

