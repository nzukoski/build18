#!/usr/bin/env python
from random import randint

class Camera(object):
	def __init__(self, id):
		self.id = id
	def __str__(self):
		return "Camera id: " + id
	def capture(self):
		#capture an image from raspicam
		return 

cam = Camera(randint(0,100))
pic = cam.capture()
#do something with pic