#!/usr/bin/env python

from fabric.api import *
from time import sleep

# globals 
env.user = "pi"
env.password = "build18"
remoteHosts = [""]

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
def getFile(id, host):	# id = remote-path/picture-id (try and specify remote absolute path on remote-host)
	env.host_string = host
	pic = get(id)
	return pic

# Display image on screen
def display(image):
	# output the image to the screen/update current
	break


# Main loop polls raspi's for images and processes running average
def main():
	average = Average()
	while(True):
		images = []
		for host in remoteHosts:	# get new images
			try:
				picId = runCommand("./camera.py", host)
				pic = getFile(picId, host)
				images.append(pic)
			except:
				print "Error: ", sys.exc_info()[0]
		# stitch images
		stitch = stitchImages(images)
		average.update(stitch)
		display(average.image)
		sleep(1)	# sleep in seconds before polling cameras

